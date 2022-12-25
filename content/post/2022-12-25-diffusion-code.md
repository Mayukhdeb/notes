+++
title = "Order From Chaos (Part 2): Diffusion for image synthesis explained in code"
date = "2022-12-25"
author = "Mayukh Deb"
tags = ["paper"]
math= true
+++

**Warning: This post is still being written and is not complete, I just uploaded a draft.**

This post is basically what I learned while watching [this video](https://www.youtube.com/watch?v=a4Yfz2FxXiY) by DeepFindr.

Diffusion models work by destroying an input gradually until it looks like noise and then recovering the input image from that. The forward process is hardcoded, and the reverse process is trainable.

We need 3 things for training a diffusion model:

1. A Scheduler that sequentially adds noise
2. A model that predicts the noise in an image (a U-Net)
3. A time-step encoding component

(WIP)
