+++
title = "Neural Taskonomy - using encodings from vision models to understand the human brain"
date = "2023-01-01"
author = "Mayukh Deb"
tags = ["paper"]
math= true
+++

## Intro

CNNs are not too bad at predicting brain activity. But using their intermediate encoding space seems to be not too effective as a way to understand the how the human brain works.

So instead of using a single CNN as a source of visual features, the authors thought that it's a good idea to build encoding models from multiple models which were trained for different vision tasks (segmentation, classification, etc).

They extracted the features describing each of the stimulus images and used them to train a model to predict brain responses. Their reasoning being: 

Given a model `M` that was trained for a task `T` (where `T` could be: segmentation, depth estimation, object detection, etc). We can infer that if an encoding from a model `M` is a good predictor of a specific brain region, information about that task `T` is likely encoded in that region.

## Method

The authors fed the image into the network and extracted an intermediate layer activation from the models. These values are used as regressors in a ridge regression model to predict brain responses to that image.

The outputs of these models are then analysed and they are basically then able to make a "matrix" of tasks, where they show that the brain-signal predictions of certain tasks are correlated, while others are not.


<!-- ## Personal notes

- Can we use a combination of these encoders to build a model which can be finetuned to make embeddings for an LLM? -->