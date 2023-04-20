+++
title = "AudioCLIP: Extending CLIP to Image, Text and Audio"
date = "2023-04-20"
author = "Mayukh Deb"
tags = ["paper"]
+++

They aim to train a tri-modal model which provides a common embedding space for 3 modalities: Images, text and Audio. The trick lies in adding in the 3rd modality (audio)

The repo can be found [here](https://github.com/AndreyGuzhov/AudioCLIP).

There are 3 components to this model:
1. Image encoder
2. Text encoder
3. Audio Encoder (ESResNeXt)

The image and the text encoder were taken from the original pre-trained CLIP model. The Audio encoder was then first pre-trained on the AudioSet dataset until it achieved a reasonably high accuracy.

Once they had a solid Audio encoder, they replaced it's classification head layer with another one whose number of output neurons is the same as the size of CLIP's embedding space. This new output head was randomly initialized.

With this new head, they start finetuning the Audio encoder in the CLIP setting, which made it's outputs compatible with the embeddings of CLIP.

---

They took 2 main approaches:

**Approach 1: train Audio-encoder only** 

The parameters of the other 2 encoders (image, text) remain frozen during this phase. The 2 frozen heads serve as teachers to the Audio encoder.

**Approach 2: train all 3 encoders** 
Reason:

The distribution of images and textual descriptions in the AudioSet dataset does not follow the one from the CLIP dataset. This led to suboptimal performance in downstream tasks

To fix this, they decided to train all of the 3 heads together on the AudioSet Dataset. This provided an additional performance boost.

**Hyperparameters**:
- Optimizer: SGD with nesterov momentum = 0.9 and weight decay = 5e-4
- Batch size: 64

The small-ness of the batch size seems counterintuitive to me. Because CLIP used a batch size of like 32k. But this proves at least in theory that we can train contrastive models with small batch sizes.