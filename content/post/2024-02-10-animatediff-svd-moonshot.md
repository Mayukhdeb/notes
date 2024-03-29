We'll explore the following 3 papers:

1. [AnimateDiff](https://arxiv.org/abs/2307.04725)
2. [SparseCtrl](https://arxiv.org/abs/2311.16933)
3. [MoonShot](https://arxiv.org/abs/2401.01827)

# AnimateDiff

They break down the objective of video generation into 2 tasks:

1. Adapt the output space of an existing text to image (T2I) model to that of the video dataset. This is done by finetuning the unet's parameters.

2. Train a "motion module" which can be integrated into the T2I model without finetuning the T2I model. This motion module's job would be to learn reasonable motion patterns from videos.

For this, they use the [webvid-10M](https://github.com/m-bain/webvid) dataset.

**Training Steps:**

1. Train a domain adapter which adapts the T2I model's output space to that of the video dataset. Somehow, this helps in avoiding the motion module from learning pixel level details in the training videos (I dont know why)
2. The T2I + Domain Adapter is then frozen.
3. Initialize and train a motion module on videos.
4. (Optional) Finetune the motion module using LoRA on custom motions/clips with a small number of video clips. They claim that ~50 videos are enough.

**Domain Adapter**

The domain adapter is used to alleviate the negative effects caused by the distribution gap between the T2I pre-training data and the video pre-training data.

The domain adapter is basically a LoRA which is inserted into the self/cross attention layers in the T2I model. The LoRA adapter is optimized on static frames randomly samples from the video dataset.

**Motion module**

The T2I model usually deals with 4D data `(batch, channels, height, width)`. But for videos, we have 5 dimensions: `(batch, frames, channels, height, width)`. We would want the T2I model to deal with each image individually. Hence they do the following einops operation to squeeze the batch and frames dim together: `(batch frames, channels, height, width) -> (batch*frames, channels, height, width)`.

This way, when the internal feature maps go through the image layers, the time dependent axis i.e `frames` is ignored.

The input of the motion module is the image feature map reshaped as: `b c h w -> (b h w) c` i.e the spatial dimensions are merged into the batch axis.

The paper does not explicitly mention what is the exact shape of the motion module transformer inputs.

**Advantages**

1. Can build on top of existing T2I models.
2. Code is available [here](https://github.com/guoyww/AnimateDiff/blob/main/train.py)

**Disadvantages**

1. Have to train 2 models. More models = more chances of things going wrong.
2. Merging spatial dims with batch dim might lead to bad spatial consistency.

# SparseCtrl

They enhance the controllability of existing text to video (T2V) models with signals that are sparse across time. They leave the original T2V model untouched.

We know how ControlNet can be used to successfully add structure control on pre-trained image generation models. They do something similar, but for videos.

Using a controlnet to do frame-by-frame guidance did not work well for temporally sparse conditioning. It was seen that only the conditioned frames were valid, and there were abrupt content changes between the conditioned and the unconditioned frames.

This inconsistency is occurring because the T2V model finds it difficult to infer the intermediate frame conditions from the sparse conditions.

The authors solve this problem by integrating a temporal layers (attention across time?) to the sparse condition encoders. This would allow the condition signal to propagate across time. This helps in propagating information from the conditioned frames to the unconditioned ones.

**Advantages**

1. Compatible with pre-trained T2V models
2. Supports conditioning in multiple modalities like sketch and depthmaps
3. Source code is [available](https://github.com/guoyww/AnimateDiff#202312-animatediff-v3-and-sparsectrl)

**Disadvantages**

1. Have to train a temporal conditioning encoder which converts sparse control signals to dense 

# Questions

**1. How come Moonshot and SVD can do img2vid natively, but aDiff requires an rgb-encoder (see SparseCtrl) to hack it into the model?**

**Answer**: AnimateDiff itself does not require an RGB encoder. It can be seen in their validation code (in [`train.py`](https://github.com/guoyww/AnimateDiff/blob/main/train.py)) how there's nothing extra required on top of the usual components.

This is the definition of their validation pipeline.

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/bb1f8f46-dd1d-45c4-9135-1b9324237c8f" width = "100%">

This is where the validation pipeline is used to generate gifs.
<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/4c600655-3a14-4271-9a3a-d9588e7ccbae" width = "100%">

The RGB image encoder is required only for sparsectrl and not for animatediff. The following quote from the sparsectrl paper helps us infer the use-case of this rgb encoder.

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/37ae7021-f2ab-4baa-a6ff-ef3ae87b776b" width = "100%">

AnimateDiff's motion module generates a video from an image. On the other hand, sparsectrl can optionally generate a video from image A to image B thanks to the conditioning information provided by the RGB image encoder.

The RGB image encoder can be used to insert one or more key-frames for guided video generation. In the image shown below, the images with a blue border are the key-frames.

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/b0675214-4e35-45b3-83d8-7184b4de12f0" width = "100%">


3. what are the training objectives used by these papers?
4. what is the framerate of these models? can we train these models on a lower framerate and use frame interpolation models like RIFE?
