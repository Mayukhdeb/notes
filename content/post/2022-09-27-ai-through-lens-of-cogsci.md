+++
title = "Watching artificial intelligence through the lens of CogSci"
date = "2022-09-27"
author = "Mayukh Deb"
tags = ["paper"]
+++

## The bias in humans interpreting functional mechanisms of a system

A paper mentions a concept called the "theory-of-mind" (Baron-Cohen et al., 1985) which mentions the fact that humans can understand that other humans have mental states like that of themselves. Our minds make up assumptions about things that are going on inside other people's minds (emotions etc).

The problem is that this bias may also bleed into the way we look into the interpretations we make of a machine. Human interpretations tend to include a lot of expectations, which are not necessary for the machine to fulfill in order to do it's job.

In a talk by Dr. Been Kim, she showed how the saliency maps from an untrained and a trained model look super duper similar. Which infers the fact that even if the interpretation of an output makes sense, it does not always mean that the model is trained.

## Insights from Perceptual and Cognitive Sciences

Humans share common semantic representations for vision and language in some brain regions. Quiroga et al. 2009 show that single neurons in the medial temporal lobe respond selectively to representations of the same individual across the visual portrait and its written name.

This suggests the fact that there is some sort of an embedding space within our minds where both images and words co-exist.

**Side note**: The "Medial Temporal lobe" is actually responsible for episodic and spatial memory

[This paper](https://vygotskian-autotelic-ai.github.io/tutorials) gives me an interesting point. Children are intrinsically motivated learners. They explore and learn things about the world on their own. On the contrary, neural networks have to be taught everything with no concept of exploration present whatsoever. What we basically do is that we show the neural nets tons of examples and hope that it learns somehting useful.

## CLIP v/s humans in image classification

Imagine an image of a dog, with the word cat written on it. This is what happens when we show the image to a human and to CLIP:

1. The human's reaction time increases because the word cat is written on the image, but it does end up giving the correct answer (i.e cat)
2. CLIP straight up says that it is a cat.

This shows that CLIP is biased towards written words over visual abstractions. This interference effect is strong when the image category is similar to the superimposed word. We can conclude that shared semantic representations of images and words disrupt image categorization. 

In humans, image categorization happens in multiple stages. Based on the representations from all modalities, a selection process decides which possible activation is the answer for the current task.

## More reading

[1] - original paper: https://developmentalsystems.org/watch_ai_through_cogsci

[2] - Vygotskian Autotelic Artificial Intelligence: https://vygotskian-autotelic-ai.github.io/