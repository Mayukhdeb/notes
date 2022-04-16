+++
author = "Mayukh Deb"
title = "How to spot a Bigfoot and an Overly Enthusiastic Comparison Between Human Perception and Multimodal Models"
date = "2021-12-25"
description = "An Overly Enthusiastic Comparison Between Human Perception and Multimodal Models"
categories = [
    "AI",
    "rambling"
]
aliases = ["an-overly-enthusiastic-comparison-between-human-perception-and-multimodal-models"]


+++
 
<!-- 
The images are kept in a github gist here:
https://gist.github.com/Mayukhdeb/830033b69f5901195cdc6f5fec26a50c#file-gistfile1-md
 -->

<img src = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bigfootlede-1563222024.jpg">

*Imagine you're chilling in your little log cabin in the woods all alone. As you start with the 2nd book of the week on a december evening, you hear a loud howl nearby. You run to the window to see what it was. Just as you look outside, you see a large shadowy figure fade into the dark woods just beyond the front yard. The information you received from your environment screams of a bigfoot encounter, but your rational mind tells you that it must be just be a tall and well built hunter, and the howl is probably some bear which got shot by the hunter*

The raw data that you received that night clearly pointed to the fact that it was a bigfoot, but then your mind found a more "rational explanation" thanks to the years of experience you have in the woods.

As elaborated in [It’s Bayes all the way up](https://www.lesswrong.com/posts/KrEwDMN4YXp5YWD45/it-s-bayes-all-the-way-up), [Corlett, Frith & Fletcher (2009)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2755113/) built a model of perception which involved a “handshake” between the Top-down and the Bottom-up ends of human perception.


## The Top-Bottom model of perception

The Top-Bottom perception model has 2 parts (of course):

1. **Bottom-Up**: Processes and infers direct conclusions from raw information coming in from the sense organs. *Scary Silhouette + Howls = bigfoot!*

2. **Top-Down**: Adds a "layer of reasoning" on top of the raw information it receives and utilizes "learned priors" (i.e experience from the past) to make sense out of the data. *Scary Silhouette + Howls = probably just a hunter who shot a bear*

![top_bottom_model](https://user-images.githubusercontent.com/53133634/148896645-0b063505-ab6e-4a10-93fb-54366d4b9ea7.png)


Kids are much more likely to "fall for" the direct consclusions made by Bottom-Up perception. This is because their Top-Down perception has not had enough "experience/training data" to learn and refine itself.

A (slightly modified) quote from [It's Bayes all the way up](https://www.lesswrong.com/posts/KrEwDMN4YXp5YWD45/it-s-bayes-all-the-way-up) summarises the process of learning in this abstraction very well:

> *"When the prediction error (loss) is too high, it registers as salience/surprise, and we focus our attention on the stimulus involved to try to reconcile the models. If it turns out that bottom-up was right and top-down was wrong, then we adjust our priors (i.e top-down perception) and so learning occurs."*

## What are Multimodal models ? 

Multimodal models are an attempt to make deep neural networks “perceive” the world in a way that’s similar to that of humans. Most of the popular deep-learning models today (Like ResNets, GPT-3, etc) are purely based for either vision or language based tasks. ResNets are good for extracting information from images, and GPTs are good at doing stuff with text. But we humans have both eyes and ears, so we are able to perceive the world through both language (by language I mean english etc) and sight. 

Multimodal models (at least in this context) are an attempt to make neural nets perceive both images and text, a great example would be OpenAI CLIP, which takes in an image and some text and returns a “confidence score” which says how much the image is “related” to the text.


## [MAGMA](https://arxiv.org/abs/2112.05253): A step towards top-bottom perception

MAGMA is a multimodal transformer which has the following goal: 

_Given a combination of text and images as input, generate the next token (i.e text)._

It can be used to answer questions related to images, some basic OCR and even identify and describe objects present in the input image(s). 

![magma_summary](https://user-images.githubusercontent.com/53133634/148896670-17fb2309-60ce-4f98-ae87-52b4d3da9d59.png)

MAGMA has 3 main components: 

1. A ResNet based image encoder which encodes images before feeding them into the rest of the model.
2. A Pre-trained Language model where we feed the input text and the encoded image(s) (example: GPT-J)
3. Adapter layers between each layer in the language model, which are trained to help “fine-tune” the language model to work well with the multimodal input. 

For the scope of this post, we can ignore the adapter layers, and just assume that we have 2 components: 

* The image encoder (henceforth referred to as IE)
* The language model (henceforth referred to as LM)


The IE can be thought of as the "eye” which helps MAGMA extract raw visual data. Much like the “bottom up” end of human perception. 

Similarly, the LM can be thought of as “the mind” which has a lot of “learned priors” which helps to make sense out of the input images and text and return an output accordingly. It is loosely equivalent to the “top-down” perception in humans. 

## How does MAGMA align with the idea of top-down perception in humans ?

![example_paris](https://user-images.githubusercontent.com/53133634/148896696-130667fe-3249-4e82-b8a0-f2cf042e2412.png)

Unless you've seen this image before, chances are high that you read it as **"I love Paris in the springtime"** and not **"I love Paris in the the springtime"** (notice how there's a second "the" in the latter). This is because your Top-Down perception read the first half of the sentence and confidently assumed that the rest of it is grammatically correct. But as we've just realised, it was wrong. 

Even though the raw data from the image tells you that there's a 2nd "the", you skip over it thanks to your top-down perception which is wired to stitch together sentences from words even without fully reading them.

Now the question is, does the same thing occur for MAGMA from a top level ? The answer is yes.

![magma_output_paris](https://user-images.githubusercontent.com/53133634/148896676-5da331ce-5906-452b-ba16-a1c432660bce.png)

When we apply interpretability methods upon this example, it becomes evident that the model does not even "look at" the 2nd "the" in the sign and moves on to complete the rest of the sentence.

![example_paris_interpret](https://user-images.githubusercontent.com/53133634/148896681-59236915-188e-4984-b33b-a99a2b8f46e1.jpg)

MAGMA is surprisingly good at OCR. I believe that a part of this ability to perceive and understand text in the world comes from the world knowledge that’s encoded in the Language model.

It is quite possible that just like humans, MAGMA also tends to “glide over” words in sentences while reading them from images by leveraging it's LM's world knowledge. Which sometimes leads to *"useful mistakes"* such as the one shown below:

<img src = "https://user-images.githubusercontent.com/53133634/149724521-6dff2a51-456f-40a9-92d1-1db7c3969489.png" width = "60%">
