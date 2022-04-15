+++
title = "Generic Attention-model Explainability"
author = "Mayukh Deb"
tags = ["paper"]
date = "2022-04-16"
+++


## Generic Attention-model Explainability for Interpreting Bi-Modal and Encoder-Decoder Transformers

Can be used to explain models like CLIP. This is how it works:

1. First, let us define an input image `x_image` and a list of input texts `[a, b, c]` where `a`, `b` and `c` can be any strings which can be tokenized and fed into the model.

    ```python
    input_texts = ["a bald man", "a rocket in space", "a man"]
    ```

2. We do a forward pass with a tokenized image and text(s) on CLIP, and obtain `logits_per_image` and `logits_per_text`. Each item within these tensors correspond to `a` and `b` and `c` respectvely.

    ```python
    {
        'logits_per_image': tensor([[22.7188, 16.1094, 23.4219]]), ## shape: 1,3
        'logits_per_text': tensor([[22.7344],[16.1250],[23.4219]]) ## shape: 3,1
    }
    ```

3. We run a softmax over `logits_per_image` on the last dim and get a nice probability map with a sum of 1 (we also convert it to numpy). Let's call it `probs`: 

    ```python
    {
        'probs': array([[3.311e-01, 4.461e-04, 6.685e-01]]
    }
    ```

4. We then choose a target `index` w.r.t which we want to find the relevance mapping. The `index` here refers to the index of one the input texts which refers to `a`, `b` or `c`.  For now, let's set `index = 0`

5. Now, we create a tensor with all zeros called `one_hot` which has the same shape as `logits_per_image` i.e `(1, 3)` and set `one_hot[0, index] = 0`. This tensor has `requires_grad` set to true which will come to play later on:

    ```python
    {
        'one_hot': tensor([[1., 0., 0.]], requires_grad=True)
    }
    ```

6. We calculate a "loss" which is defined as shown below and do a backward pass over through the model. `one_hot * logits_per_image` masks `logits_per_image` to only include the logit corresponding to `index`. So in this case `loss = 22.7188`

    ```python
    loss = torch.sum(one_hot * logits_per_image)
    model.zero_grad()
    loss.backward(retain_graph=True)
    ```

7. Now, let us assume that we have `n` layers in the model with attention outputs. Out of which we select the last layer for our work, let us call it `block`. The output of the attention layer would be a 3D tensor of shape which looks something like: `[12, 50, 50]`.  We select a subset of these layers for our experiments.

8. We make an identity matrix `R` (probably means to "results") of shape `(d , d)` where `d` is the length of the last dim of the attention outputs of the model. In this case, `d` is 50.

9. Using forward and backward hooks, we capture the outputs of the attention layer(s) into 2 attributes both of which have shape `(12, 50, 50)`:

    *  `block.attn_probs` (forward hook): stores the attention outputs post softmax + dropout. 
    * `block.attn_grad` (backward hook): stores the gradients of the same outputs w.r.t the loss. It tells us `d(loss)/d(block.attn_probs)`. 

10. we do the following with `block.attn_probs` and `block.attn_grad` iteratively for each `block`:

    ```python
    y = block.attn_probs * block.attn_grad  ## y.shape = (12, 50, 50)
    y = cam.clamp(min=0).mean(dim=0)  ## y.shape = (50,50)
    R += torch.matmul(cam, R)  ## R.shape = (50,50) 
    ```

11. We then set `R[0, 0] = 0` for some reason which I'm not sure of rn. 

12. Then we obtain a 2D heatmap by selecting a specific subset of `R` which is `R[0, 1:]` (which comes to be of shape `(49,)`) and reshape it to `(7,7)`.

13. Finally, we scale this heatmap and resize it to be of the same height and width as of the original input image. 

## Resources:

* [original paper](https://arxiv.org/pdf/2103.15679.pdf)
* [original implementation on github](https://github.com/hila-chefer/Transformer-MM-Explainability)

 