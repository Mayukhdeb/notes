+++
title = "Parti - Scaling LLMs for Text to Image tasks"
date = "2022-08-07"
author = "Mayukh Deb"
tags = ["paper"]
+++

# Scaling Autoregressive Models for Content-Rich Text to Image Generation

The architecture itself that's used for parti (that's what the authors call this model) is fairly simple. It's a transformer encoder-decoder architecture paired with a ViT VQGAN in the end to tokenize/detokenize images.

## How do we tokenize images?

For an autoregressive model to work, we basically have to convert everything to tokens. Tokenizing text is super easy. The problem in this case is that we also have to convert images into a sequence of tokens.

This tokenization of images is done by the VQGAN tokenizer. I have explained how this happens in one of my [old blog posts](https://mayukhdeb.github.io/blog/post/an-image-is-worth-16-x-16-explained/#how-do-we-tokenize-images-).

The "Q" in VQGAN refers to quantized. The token space of the VQGAN is "quantized" to roughly 8k tokens. I think I should read the ViT VQGAN paper in case I ever have to work on image generation (which I hope might be soon).

## How do we train such a model?


Essentially, we do the following for training:

1. First, we assume that the input is a text, image pair `(T, I)`. 
2. We tokenize `I` using the ViT-VQGAN image tokenizer.
3. We tokenize text and feed it into the transformer encoder.
4. We feed the sequence of tokens of the image `[<SoT>, i1, i2, ..., iM]` (`M` image patches) into the transformer decoder (along with a start of sentence `<SoT>` token).
5. We take the transformer-decoder's outputs and feed it to the image-detokenizer of the ViT-VQGAN.
6. The image detokenizer re-constructs the image which was on the input. Let's call it `I_reconstructed`.
7. The model basically gets trained as an image reconstruction model. Which later would be used for image generation somehow.

## WIP


## Resources

1. ViT + VQGAN paper: https://arxiv.org/abs/2110.04627
2. Parti paper: https://arxiv.org/abs/2206.10789



