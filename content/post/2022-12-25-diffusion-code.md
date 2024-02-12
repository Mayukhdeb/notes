**Warning: This post is still being written and is not complete, I just uploaded a draft.**

This post is basically what I learned while watching [this video](https://www.youtube.com/watch?v=a4Yfz2FxXiY) by DeepFindr.

Diffusion models work by destroying an input gradually until it looks like noise and then recovering the input image from that. The forward process is hardcoded, and the reverse process is trainable.

In the reverse process, the task of the model is to predict the noise that was added in each step to the input image.

We need 3 things for training a diffusion model:

1. A Scheduler that sequentially adds noise
2. A model that predicts the noise in an image (a U-Net)
3. A time-step encoding component

## The forward process

{{< math.inline >}}
<p>
In simple words, we iteratively add noise into the image where the amount of noise added per step is dependent on a parameter \(\beta\)
</p>
{{< /math.inline >}}

In fancy math terms, this is how we perform the markov process:

$$
  q(x_{1:T}|x_0) = \prod_{t=1}^{t=T}q(x_t|x_{t-1})
$$

{{< math.inline >}}
<p>
\(x_{1:T}\) =  set of samples where every subsequent item is noisier starting from the orignial image. \(x_1\) is the input image after adding some noise for the first time (i.e the first step) and \(x_T\) is the most noisy sample.
</p>

<p>
\(\prod_{t=1}^{t=T}q(x_t|x_{t-1})\) is the product of the noise samples for all values of \(t\) starting from 1 to \(T\)
</p>
{{< /math.inline >}}

**Diving deeper into each noise sample {{< math.inline >}}\(q(x_t|x_{t-1})\){{</ math.inline >}}**

First, let's see how it's defined:

$$
 q(x_t|x_{t-1}) = N(x_t;\sqrt{1-\beta_t}x_{t-1}, \beta_tI) 
$$

* {{< math.inline >}}
<p>
\(\beta_t\) determines the variance of the noise to be added in each step into the image. 
</p>
{{< /math.inline >}}

* {{< math.inline >}}
<p>
\(x_{t-1}\) is the previous less noisy image. 
</p>
{{< /math.inline >}}

* {{< math.inline >}}
<p>
\(\sqrt{1 - \beta_t}\) scales the mean of the noise to be added. Thus one can say that the mean of our distribution is \(\sqrt{1-\beta_t}\) multiplied by \(x_{t-1}\) (for each pixel).
</p>
{{< /math.inline >}}

* {{< math.inline >}}
<p>
\(I\) is the Identity
</p>
{{< /math.inline >}}

{{< math.inline >}}
<p>
The sequence of such betas \(\beta_1\), \(\beta_2\)... \(\beta_t\) is known as the variance schedule. They determine how much noise we'd want to add in each of the time steps.
</p>
{{< /math.inline >}}

**Diving deeper into {{< math.inline >}}\(\beta\){{</ math.inline >}}**

Let us imagine for a second that we have an image with a single pixel and then try to understand what then equation above means:

{{< math.inline >}}
<p>
\(q(x|x_{t-1})\) = the value of the next pixel (q of \(x\) given \(x_{t-1}\))
</p>
{{< /math.inline >}}

<center>
<img src = 'https://user-images.githubusercontent.com/53133634/209522028-ad0081b5-c233-4039-8d80-8a399f94c7a3.png' width = "40%">
Image taken from DeepFindr's video[1] at 8m47s.
</center>

* {{< math.inline >}}
<p>
\(\mu\) is the mean of the dstribution from which we would sample the next pixel
</p>
{{< /math.inline >}}

* {{< math.inline >}}
<p>
\(\sigma\) is the variance.
</p>
{{< /math.inline >}}

{{< math.inline >}}
So increasing \(\beta\) would result in the distribution shifting to the left and also becoming more flattened (w i d e r). Kind of like the blue distribution shown below.
{{< /math.inline >}}

<center>
<img src = 'https://user-images.githubusercontent.com/53133634/209523096-53d22a91-6c9a-4af7-9c74-b683b39b9749.png' width = "40%">
Image taken from DeepFindr's video[1] at 9m28s.
</center>

Beta determines how fast we converge towards a mean of zero which is basically a standard gaussian distribution. Beta increases linearly with each time step (from like `0.0001` to `0.02` in 200 steps)

### Speeding things up

{{< math.inline >}}
<p>
The neat thing about gaussians is that the sum of gaussians is also a gaussian. Which means it's pretty easy to pre-compute the noisy image at forward time-step \(t\)
</p>

<p>
Now for convenience, we would make a new variable \(\alpha_t = 1 - \beta_t\). Since beta was being scaled up, alpha would be scaled down on each step. You can think of alpha as the variable which determines how much information is conserved from the previous image in each time step.
</p>
<p>
The nice part is that we can just take the cumulative products of alpha (\(\bar{\alpha_t}\)) and then we can compute the image at a forward step \(t\) without having to calculate all the way until step \(t-1\) first. This way, we can re-define the noise sampling as follows:
</p>
{{< /math.inline >}}

$$
 q(x_t|x_{t_0}) = N(x_t;\sqrt{\bar{\alpha_t}}x_{0}, (1 - \bar{\alpha_t})I) 
$$

{{< math.inline >}}
Notice how this function is dependend only on \(x_0\) and not on \(x_t\) but it computes the noisy pixel value at time step \(t\).
{{< /math.inline >}}

### Finally, some code

I'll try to explain things line-by-line:

```python
import torch
import torch.nn.functional as F

def linear_beta_schedule(timesteps, start=0.0001, end=0.02):

    ## Interpolates between 2 values with a pre-defined number of timesteps. 
    ## Returns a list of Betas
    return torch.linspace(start, end, timesteps)

def get_index_from_list(vals, t, x_shape):
    """ 
    Returns a specific index t of a passed list of values vals
    while considering the batch dimension.
    """
    batch_size = t.shape[0]
    out = vals.gather(-1, t.cpu())
    return out.reshape(batch_size, *((1,) * (len(x_shape) - 1))).to(t.device)

def forward_diffusion_sample(x_0, t, device="cpu"):
    ## takes the input image and the timestep number t as input
    ## and returns it's noisy version at timestep t
    noise = torch.randn_like(x_0)
    sqrt_alphas_cumprod_t = get_index_from_list(sqrt_alphas_cumprod, t, x_0.shape)
    sqrt_one_minus_alphas_cumprod_t = get_index_from_list(
        sqrt_one_minus_alphas_cumprod, t, x_0.shape
    )
    # mean + variance
    return sqrt_alphas_cumprod_t.to(device) * x_0.to(device) \
    + sqrt_one_minus_alphas_cumprod_t.to(device) * noise.to(device), noise.to(device)

```

The last line in the above snippet is equivalent to:

$$
 x_t = \sqrt{\bar{\alpha_t}}x_0 + \sqrt{1-\bar{\alpha_t}}\epsilon
$$

{{< math.inline >}}
Where \(\epsilon\) is the noise added into the image.
{{< /math.inline >}}

Then, we pre-compute the variables for convenience:

```python
alphas = 1. - betas
alphas_cumprod = torch.cumprod(alphas, axis=0)
alphas_cumprod_prev = F.pad(alphas_cumprod[:-1], (1, 0), value=1.0)
sqrt_recip_alphas = torch.sqrt(1.0 / alphas)
sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod)
sqrt_one_minus_alphas_cumprod = torch.sqrt(1. - alphas_cumprod)
posterior_variance = betas * (1. - alphas_cumprod_prev) / (1. - alphas_cumprod)
```

## The Neural network

The authors proposed to use a a U-Net, which is an image-to-image model. Here the input is the noisy image, and the output is the "noise" predicted by the model. 

{{< math.inline >}}
So if we have an input \(x_t = x0 + \epsilon\) then the model's output would ideally be \(\epsilon\) or something close to it.
{{< /math.inline >}}

## Encoding time steps

Note that we also have to let the model know in which timestep the input image is, this is done with the help of positional embeddings.

```python
class SinusoidalPositionEmbeddings(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, time):
        device = time.device
        half_dim = self.dim // 2
        embeddings = math.log(10000) / (half_dim - 1)
        embeddings = torch.exp(torch.arange(half_dim, device=device) * -embeddings)
        embeddings = time[:, None] * embeddings[None, :]
        embeddings = torch.cat((embeddings.sin(), embeddings.cos()), dim=-1)
        return embeddings
```

**Intuition behind `SinusoidalPositionEmbeddings`**

(btw this also applies to transformers in general)

To understand this, first let's take a look at how binary numbers work. You might be able to notice here that the right-most bit (red) oscillates between 0 and 1 the fastest and the subsequent ones (blue, green, yellow) oscillate in slower and slower rates.

<center>
<img src = "https://user-images.githubusercontent.com/53133634/209769905-70663f7f-aa2c-4ee6-9fd3-590f4245b089.png" width = "50%">
</center>

Now if we use these values as positional encodings, the last 2 bits are good at giving fine-grained relative positions between 2 positions which are close to each other. While the larger bits are good at encoding the position at a larger scale. This way, the model would get both the overall location of each token but would also be able to distinguish between tokens which are very close to each other.


But in real life, binary numbers take up lots of space. So instead we use the something fancier: Sinusoids.

<center>
<img src = "https://user-images.githubusercontent.com/53133634/209771097-1e970289-bfbc-4624-bad6-639f98aac172.png" width = "100%">
</center>

In the figure above, you can see how the first column (left) oscillates the fastest and every column after that one oscillates slower and slower. These are sinusoidal positional embeddings with a depth of 128.

## Combining time-step encoding with image data

I will not go into depth about the U-Net architecture itself, because it can be and has been replaced with other models for diffusion. You can just think of it as a model which takes an image as an input and is supposed to predict the noise in the input (which gets subtracted).

The important thing to note here is that we do not concatenate the time embeddings into the data, instead we add it right after passing the input through the first conv layer of a U-Net block.

```python
class Block(nn.Module):
    """
    A single building block from the U-Net
    """
    def __init__(self, in_ch, out_ch, time_emb_dim, up=False):
        super().__init__()
        self.time_mlp =  nn.Linear(time_emb_dim, out_ch)
        if up:
            self.conv1 = nn.Conv2d(2*in_ch, out_ch, 3, padding=1)
            self.transform = nn.ConvTranspose2d(out_ch, out_ch, 4, 2, 1)
        else:
            self.conv1 = nn.Conv2d(in_ch, out_ch, 3, padding=1)
            self.transform = nn.Conv2d(out_ch, out_ch, 4, 2, 1)
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1)
        self.bnorm1 = nn.BatchNorm2d(out_ch)
        self.bnorm2 = nn.BatchNorm2d(out_ch)
        self.relu  = nn.ReLU()
        
    def forward(self, x, t, ):
        # First Conv
        h = self.bnorm1(self.relu(self.conv1(x)))
        # Time embedding
        time_emb = self.relu(self.time_mlp(t))
        # Extend last 2 dimensions
        time_emb = time_emb[(..., ) + (None, ) * 2]
        '''
        This is where we add in the time embedding
        combines time step and image information
        '''
        h = h + time_emb
        # Second Conv
        h = self.bnorm2(self.relu(self.conv2(h)))
        # Down or Upsample
        return self.transform(h)
```

## Loss function

The loss function is basically the L1 loss on the predicted noise v/s the original noise:

```python
def get_loss(model, x_0, t):
    """
    model: U-Net model through which we pass the image
    x_0: original input image
    t: a specific time step

    functions within:
        * forward_diffusion_sample: returns the noisy version of the original image and the noise that was last added for the time step t
        * model.__call__: takes as input the noisy image and the time step, tries to predict the noise that was last added for the time step t
    """
    x_noisy, noise = forward_diffusion_sample(x_0, t, device)
    noise_pred = model(x_noisy, t)
    return F.l1_loss(noise, noise_pred)
```


## Sampling

TODO: explain this

```python
@torch.no_grad()
def sample_timestep(x, t):
    """
    Calls the model to predict the noise in the image and returns 
    the denoised image. 
    Applies noise to this image, if we are not in the last step yet.
    """
    betas_t = get_index_from_list(betas, t, x.shape)
    sqrt_one_minus_alphas_cumprod_t = get_index_from_list(
        sqrt_one_minus_alphas_cumprod, t, x.shape
    )
    sqrt_recip_alphas_t = get_index_from_list(sqrt_recip_alphas, t, x.shape)
    
    # Call model (current image - noise prediction)
    model_mean = sqrt_recip_alphas_t * (
        x - betas_t * model(x, t) / sqrt_one_minus_alphas_cumprod_t
    )
    posterior_variance_t = get_index_from_list(posterior_variance, t, x.shape)
    
    if t == 0:
        return model_mean
    else:
        noise = torch.randn_like(x)
        return model_mean + torch.sqrt(posterior_variance_t) * noise 
```

## References

[1] - [DeepFindr's video](https://www.youtube.com/watch?v=a4Yfz2FxXiY)
