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

## The Forward process

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

(WIP)

## The Backward process

## References:

[1] - https://deepai.org/machine-learning-glossary-and-terms/gaussian-distribution

