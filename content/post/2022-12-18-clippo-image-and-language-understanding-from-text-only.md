+++
title = "CLIPPO: Image and Language understanding from pixels only"
date = "2022-12-18"
author = "Mayukh Deb"
tags = ["paper"]
+++

## CLIP v/s CLIPPO

- CLIP trains 2 seperate image and text encoders, each with it's own preprocessing and embeddings. 
- CLIPPO trains a single transformer where the images are sent in as images and the text is also rendered as a image before shoving it into the forward pass


**How do they render text as an image?**

Text inputs are rendered on blank images, and are subsequently dealt with entirely as images. They literally just "write" the text on a blank image and then just treat it as an image. An accidental advantage of this kind of a method is that it removes the need for a tokenizer.

A common loss objecive used in these kinds of tasks is the contrastive loss.

## What is a contrastive loss?

When training models on Image/alt-text pairs, two encoders are usually trained with a contrastive loss, encouraging the embeddings of corresponding images and alt-text to be similar, and at the same time to be dissimilar from all other image and alt-text embeddings.

## My noob opinions

- in a way, CLIPPO is the anti-MAGMA. They adopt the text to the image space, while MAGMA adopts the image to the text (embedding) space (but I'm not sure how much of a modality gap[1] we have on MAGMA)

**Questions**
- what about text prompts which are too long? what do you do then?
- can we move smoothly between visual concepts by interpolating the "image containing the text"?

## References:
1. [Interesting related paper on "modality gaps"](https://arxiv.org/pdf/2203.02053.pdf)
