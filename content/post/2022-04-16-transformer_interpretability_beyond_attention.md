+++
title = "Transformer intrepretability beyond attention "
date = "2022-04-16"
author = "Mayukh Deb"
tags = ["paper"]
+++

# Transformer intrepretability beyond attention 

## Disadvantages of attention rollout and LRP

Irrelevant tokens often get highlighted

The main challenge in assigning attributions based on attentions is that attentions are combining non-linearly from one layer to the next. The rollout method assumes that attentions are combined linearly and considers paths along the pairwise attention graph. We observe that this method often leads to an emphasis on irrelevant tokens since even average attention scores can be attenuated. The method also fails to distinguish between positive and negative contributions to the decision.

Transformers apply activation functions other that ReLU, which result in both positive and negative features. Because of the non-positive values, skip connections lead, if not carefully handled, to numerical instabilities. Methods such as LRP for example, tend to fail in such cases.

## How does this method beat the methods mentioned above then ?

* Filters out negative contributions to the decision (unlike attention rollout)

* Considers the fact that transformers use non-linearities which have negative output values such as GeLU, where LRPs generally fail.

    * Non-linearities other that ReLU, such as GELU, output both positive and negative values. To address this, LRP propagation can be modified by constructing a subset of indices we consider only the elements that have a positive weighed relevance.
