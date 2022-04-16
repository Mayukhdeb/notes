+++ 
title = "Attention Rollout"
author = "Mayukh Deb"
tags = ["paper"]
date = "2022-04-16"
+++

## How is it better than just viewing raw attention maps ? 

Viewing raw attention maps as a way to explain transformers does not take into account the fact that we also have residual connections in the model. When we only use attention weights to approximate the flow of information in Transformers, we ignore the residual connections. But these connections play a significant role in tying corresponding positions in different layers.

## Refined method

One drawback of the original attention rollout method was that it was focused primarily on tasks which involved predicting only the "next" token/any process which involved only one forward pass (like predicting pronouns). 

In order to make this method work in our use-case i.e generative LM's, we can iteratively keep track of the attention rollout values while generating `n` tokens. This would enable us to understand how much each generated token is "correlated" to the original prompt. 

On a lower level, the process does the following: 

1. Given `m` input tokens, we generate `n` more tokens i.e `n` forward passes
2. On each step, we register the attention rollout values. For the `i`th step, the size of the attention rollout matrix would be: `[m + i, l]` where `l` = number of layers with attention outputs in the model. 
3. Slice every obtained attention matrix along the last dim as `[:m, :]` (only include values corresponding to the input tokens). 
4. Concatenate all of the obtained sliced matrices along dim 0. Thus giving us a matrix `M` of shape: `[n, m, l]` where:

    * `n` = number of generated tokens
    * `l` = number of layers with attention outputs in the model
    * `m` = number of tokens in original prompt

5. Then in order to analyse all the input tokens w.r.t a generated token, we can slice the matrix as `M[index_of_generated_token, :, :]`.


## Drawbacks

A higher attention rollout value does not necessarily infer to the token being "important" for a prediction. This method in it's raw form tends to be biased towards common english words and punctuations (`[",", ".", "\n", "is", ":". "and"]`), which might lead to skewed or non-intuitive results. This makes it necessary for the user to filter out these tokens in order to make sense out of the values.

## Resources/links

* [Original paper](https://arxiv.org/abs/2005.00928)
