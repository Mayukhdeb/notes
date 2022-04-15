+++
title = "Interpreting LMs with contrastive explanations"
author = "Mayukh Deb"
tags = ["paper"]
date = "2022-04-16"
+++


## Interpreting language models with contrastive explanations

interpretability methods commonly used for other NLP tasks like text classification, such as gradient-based saliency maps are not as informative for LM predictions

In general, language modeling has a large output space and a high complexity compared to other NLP tasks; at each time step, the LM chooses one word out of all vocabulary items. This contrasts with text classification (where the output space is smaller).

Contrastive explanations aim to identify causal factors that lead the model to produce one output instead of another output

Contrastive explanations attempt to explain why given an input x the model predicts a target yt instead of a foil yf

Erasure-based methods measure how erasing different parts of the input affects the model output (Li et al., 2016b). This can be done by taking the difference between the model output with the full input x and with the input where xi has been zeroed out.


Gradient Norm and Contrastive Gradient Norm do not provide information on directionality