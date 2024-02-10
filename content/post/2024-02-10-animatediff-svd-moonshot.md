+++ 
title = "Video Generation Models"
author = "Mayukh Deb"
tags = ["paper"]
date = "2024-02-10"
+++

We'll explore the following 3 papers:
1. [AnimateDiff](https://arxiv.org/abs/2307.04725)
2. [SparseCtrl](https://arxiv.org/abs/2311.16933)
3. [MoonShot](https://arxiv.org/abs/2401.01827)

# AnimateDiff

**Method**
They propose a motion module which can be integrated into an existing text-to-image (T2I) model without the need of any finetuning of the T2I model. This motion module knows how to convert the generated images into videos.

They also propose a MotionLoRA module which can be used to customize the motion module on personalized videos.

The motion module learns reasonable motion priors from videos.

They use the webVid 10M dataset.

Steps:
1. train a domain adapter which adapts the T2I model's output space to that of the video dataset. Somehow, this helps in avoiding the motion module from learning pixel level details in the training videos (I dont know why)
2. The T2I + Domain Adapter is then frozen
3. We initialize and train a motion module on videos.
4. Optional step. We finetune the motion module using LoRA on custom motions/clips with a small number of video clips. They claim that ~50 videos are enough.

**Domain Adapter**

The domain adapter is used to alleviate the negative effects caused by the distribution gap between the T2I pre-training data and the video pre-training data.

The domain adapter is basically a LoRA which is inserted into the self/cross attention layers in the T2I model. The LoRA adapter is optimized on static frames randomly samples from the video dataset.

**Motion module**

The T2I model usually deals with 4D data `(batch, channels, height, width)`. But for videos, we have 5 dimensions: `(batch, frames, channels, height, width)`. We would want the T2I model to deal with each image individually. Hence they do the following einops operation to squeeze the batch and frames dim together: `(batch frames, channels, height, width) -> (batch*frames, channels, height, width)`.

This way, when the internal feature maps go through the image layers, the time dependent axis i.e `frames` is ignored.

**Advantages**

**Disadvantages**

I'll be trying to answer the following questions:
1. 