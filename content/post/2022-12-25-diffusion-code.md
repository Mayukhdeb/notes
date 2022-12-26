+++
title = "Order From Chaos (Part 2): Diffusion for image synthesis explained in code and a little bit of math"
date = "2022-12-25"
author = "Mayukh Deb"
tags = ["paper"]
math= true
+++

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

Beta determines how fast we converge towards a mean of zero which is basically a standard gaussian distribution.

## Speeding things up

{{< math.inline >}}
The neat thing about gaussians is that the sum of gaussians is also a gaussian. Which means it's pretty easy to pre-compute the noisy image at forward time-step \(t\)
{{< /math.inline >}}

## References

[1] - [DeepFindr's video](https://www.youtube.com/watch?v=a4Yfz2FxXiY)
