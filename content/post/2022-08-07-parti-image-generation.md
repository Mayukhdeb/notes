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

Another thing to note, is that the paper mentions that they used an image upscaling model to resize the output image from 256x256 to 1024x1024.

## Inference

1. This time the input is just a piece of text i.e a "prompt"
2. We feed the text into the transformer encoder, and feed the `<SoT>` token into the transformer decoder.
3. The decoder then generates the first output image patch token `i1`
4. We then feed `[<SoT>, i1]` into the transformer decoder and obtain `i2`. 
5. We keep repeating steps 3 and 4 with inputs `[<SoT>, i1, i2, i3 ...]` until we reach `iM` where `M` is the number of image patches required to construct one image.
6. Once we have a set of output image patch tokens `[i1, i2, i3, ...iM]`, we feed it into the ViT-VQGAN  image detokenizer and obtain the "generated" image.

In a nutshell, we autoregressively generate image tokens with the decoder.

## Other notes

The largest possible model they trained was a 20B param model. Yannic was saying that complaining about not have the exact composition on the generated images is already like "moving the goal post" at this point, given how far we've come from the 2018 styleGAN era.

I am barely educated to make comments on how good parti or DALLE2 is, but what I understand is that words are a very lossy way to compress an idea of an image.

You can compress a picture of a cat in a tree with "cat in tree", the decompression just generates a picture of a cat in a tree, the loss is that it may be a different cat in a different tree.

My opinion is that in order to solve the problem of compositionality, it makes sense to look into the model itself and it's mechanisms instead of just "going bigger". 

Going big is what companies with deep pockets like openAI/Google can do. But to me it also sounds like a rather lazy solution, given how little effort people put into understanding these black-box-y systems.

## Resources

1. ViT + VQGAN paper: https://arxiv.org/abs/2110.04627
2. Parti paper: https://arxiv.org/abs/2206.10789



