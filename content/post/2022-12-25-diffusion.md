+++
title = "Order From Chaos: Diffusion for image synthesis"
date = "2022-12-25"
author = "Mayukh Deb"
tags = ["paper"]
math= true
+++

**Warning: This post is still being written and is not complete, I just uploaded a draft.**

## Intro

If you take and image and iteratively add very small amounts of noise to it, eventually the image would be unrecongnizable to the eye -- Now what if we could undo this process?

Start from noise, and then iteratively remove the noise until you end up with the real image again.

## The Forward and backward processes

{{< math.inline >}}

Given an image \(X_0\), we would want to convert it to \(X_T\) by gradually adding noise to \(X_0\) in \(T\) time steps.

{{</ math.inline >}}

$$
 X \rightarrow X_T 
$$

{{< math.inline >}}
<p>
We do this by adding a small amount of noise (let's call this a "step"). The forward process is basically a markov chain, where the output of step \(n\) only depends on the sample from the \(n-1\)th step.
</p>
{{</ math.inline >}}


{{< math.inline >}}
<p>

We would formulate this forward process such that when \(T\) approaches \(\infty\), \(X_T\) would approach a gaussian distribution[1] with center at 0, and would lose all information from the original image.

In real life, \(T\) is generally in the order of 1000.

</p>
{{</ math.inline >}}

{{< math.inline >}}
<p>

The step sizes are controlled by a variance schedule \(\beta_T\) which is generally chosen to be super small, making sure that only a small amount of noise is added in each forward step. This is so that it is not too hard for the model to remove the noise in each step in the reverse process.

</p>
{{</ math.inline >}}

Different forward time steps are associated with different noise levels, and the model can learn to undo these individually.

{{< math.inline >}}
<p>
The backward process from \(X_T\) to \(X\) is also a markov chain where \(X_{T-n}\) depends on \(X_{T-(n-1)}\) and so on.
</p>
{{</ math.inline >}}

## More insight

What we saw so far is the following:

1. The Forward process is basically a way to iteratively push a sample off the overall data manifold (domain)

2. The reverse process then produces a trajectory back into the manifold to create a "real sample".

{{< math.inline >}}
<p>
A diffusion model might mildly remind someone of the variational autoencoder. Where we first encoded an input variable \(X\) to become \(Z\) and then decoded it to obtains \(\tilde{X}\) which is supposed to a reconstruction of \(X\).
</p>
The image below shows the similarity very nicely.
{{</ math.inline >}}

<img src = "https://user-images.githubusercontent.com/53133634/209469123-81d3fc54-151e-4398-9cec-e3a741bd26d7.png">

Image taken from Ari Seff's video[2] ([this frame](https://youtu.be/fbLgFrlTnGU?t=406)) which I'd highly recommend watching.

But unlike VAEs, in diffusion models, the encoding part is not trained or is trainable. It is only the reverse decoding part that gets trained.

## References:

[1] - Gaussian distribution explained: https://deepai.org/machine-learning-glossary-and-terms/gaussian-distribution

[2] - Ari Seff's video: https://www.youtube.com/watch?v=fbLgFrlTnGU

