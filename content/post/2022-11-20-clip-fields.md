+++
title = "VPT: Video Pre-Training on Minecraft"
date = "2022-12-18"
author = "Mayukh Deb"
tags = ["paper"]
+++

## Pseudo labelling

There are 4 main stages in the data collection stage:

1. First, they paid some contractors and obtained 2k hours of labelled minecraft gameplay data. This contained the video frames from within the game and the respective player action (key press, mouse movement). This in total gave them 2k hours of data.

2. Then they scrape minecraft videos from youtube and keep only the clean ones. Clean = does not contain the face of the streamer in the corner etc.

3. Take the data from stage 1 and train an "Inverse Dynamics Model" (IDM).

4. Use the IDM to label the large unlabeled dataset.

## What is an inverse dynamics model?

Just how Autoregressive models are next-token predictors, IDM models are mid-token predictors. 

In IDMs, the model can "pay attention" to both the past and the future tokens and predict the token in between. This seems to be a much easier task than that of predicting the next token.

Given below is an example which further demonstrates the difference. 

- `{x}` = unknown token which is to be predicted.
- Dataset = `{He}{likes}{burgers}{and}{fries}`

| Model            | Input                                        | Target Output                            |
|------------------|----------------------------------------------|------------------------------------------|
| Autoregressive   | `{He}{likes}{Burgers}{and}`             | `{likes}{Burgers}{and}{fries}`                                  |
| Inverse Dynamics | `{He}{likes}{x}{x}{fries}` | `{He}{likes}{Burgers}{and}{fries}` |
| Inverse Dynamics | `{He}{x}{Burgers}`                 | `{He}{likes}{Burgers}`             |

**Note:** As seen above in the table, I explained it with a text example, but in the paper it was player actions, not text.

## Training

Once we have the synthetically labelled dataset, we then use the same architecture as the IDM but this time we make it causal (i.e like GPT) and train it on this dataset.

Each forward pass involves the following:

1. Take 5 consecutive gameplay frames and run them over a 3D convolution. The pass it through some more stuff to obtain embeddings

2. train a transformer decoder which predicts the "next action" to be taken

Once they obtain a powerful base model, they finetune it with RL on various kinds of tasks like making a picaxe etc.
