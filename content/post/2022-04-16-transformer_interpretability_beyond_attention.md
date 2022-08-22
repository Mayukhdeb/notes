+++
title = "Transformer intrepretability beyond attention"
date = "2022-04-16"
author = "Mayukh Deb"
tags = ["paper"]
+++

## Disadvantages of attention rollout and LRP

Irrelevant tokens often get highlighted

The main challenge in assigning attributions based on attentions is that attentions are combining non-linearly from one layer to the next. The rollout method assumes that attentions are combined linearly and considers paths along the pairwise attention graph. We observe that this method often leads to an emphasis on irrelevant tokens since even average attention scores can be attenuated. The method also fails to distinguish between positive and negative contributions to the decision.

Transformers apply activation functions other that ReLU, which result in both positive and negative features. Because of the non-positive values, skip connections lead, if not carefully handled, to numerical instabilities. Methods such as LRP for example, tend to fail in such cases.

## How does this method beat the methods mentioned above then ?

* Filters out negative contributions to the decision (unlike attention rollout)

* Considers the fact that transformers use non-linearities which have negative output values such as GeLU, where LRPs generally fail.

* Non-linearities other that ReLU, such as GELU, output both positive and negative values. To address this, LRP propagation can be modified by constructing a subset of indices we consider only the elements that have a positive weighed relevance.

## Experiments

**Models**:
1. linguistic classification task: BERT base model
2. visual classification: ViT base model

**Evals**:
1. Visual:
    - [A benchmark for interpretability methods in deep neural networks](https://arxiv.org/abs/1806.10758) on validation set of ImageNet (ILSVRC) 2012, consisting of 50K images from 1000 classes
    - ImageNet-Segmentation, containing 4,276 images from 445 categories
2. Linguistic
    - Movie reviews dataset from the [ERASER](https://www.eraserbenchmark.com/) dataset. (Nite that the The BERT model is first fine-tuned on the training set of the Movie Reviews Dataset and the various evaluation methods are applied to its results on the test set.)

**Metrics**:
1. Visual (segmentation)
    - pixel-accuracy, obtained after thresholding each visualization by the mean value
    - mean-intersection-over-union (mIoU)
    - mean-Average-Precision (mAP)
2. Linguistic:
    -  they use the token-F1 score, which is best suited for pertoken explanation (in contrast to explanations that extract an
excerpt)

Other notes from their evals:
- To best illustrate the performance of each method, they consider a token to be part of the “rationale” if it is part of the top-k tokens, and show results for k = 10 . . . 80 in steps of 10 tokens. This way, they do not employ thresholding that may benefit some methods over others.


