+++ 
author = "Mayukh Deb" 
title = "Hello World" 
date = "2021-10-24" 
description = "How and why I started writing code" 
tags = [ 'past' ] 
categories = [ "past", ] 
aliases = ["hello-world"] 
+++




# Attention Rollout for explaining transformers 

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


    <img src = "images/attention_flow/refined_method.png" width = "90%">

## Examples

### Names

| prompt | completion | selected output token | attention rollout values (mean along layer dim) |
|--------|------------|--------------------|---------------------------------------------|
|   My name is Putin, I am from     |        Russia, I am a Russian      | Russia               |        <img src = "images/attention_flow/putin_russia.png" width = "80%">                                   |
|    My name is Abdul, I am from    |       Pakistan. I am a student of the University of Delhi     | Pakistan                |                   <img src = "images/attention_flow/abdul_pak.png" width = "80%"> 

---
### Question answering

```
Context: It is sunny today, which is bad.
Q: How is the weather today ?
A: It is
```

Completion
```
 sunny, but it is not as warm as it was yesterday.
```

Attention rollout visualizations for completion token `sunny` shows that the top 3 input tokens are: 

1. `sunny`
2. `weather`
3. `How`

The 2D representation of the same visualization also shows us that the attention rollout value of the input token `17: weather` spikes at layer number 20, while the input token `4: sunny`'s attention rollout values are relatively more spread out accross the layers. 

| output token | mean  | original |
|--------------|-------|----|
| `sunny` | <img src = "images/attention_flow/context_sunny_mean.png" width = "100%">                |       <img src = "images/attention_flow/context_sunny_2d.png" width = "100%">                   |


---

### Long prompt

Prompt:

```
The grandest and most renowned of all these is the Colosseum at Rome. It was built by David and his son Titus, the conquerors of Egypt.
Q: Who built the Coliseum ?
A:
```

Completion
```
The Colosseum was built by David
```

| output token | mean  | original |
|--------------|-------|----|
| `David` | <img src = "images/attention_flow/qna_rome.png" width = "100%">                |       <img src = "images/attention_flow/qna_rome_2d.png" width = "100%">                   |


## Drawbacks

A higher attention rollout value does not necessarily infer to the token being "important" for a prediction. This method in it's raw form tends to be biased towards common english words and punctuations (`[",", ".", "\n", "is", ":". "and"]`), which might lead to skewed or non-intuitive results. This makes it necessary for the user to filter out these tokens in order to make sense out of the values.

## Resources/links

* [Try it yourself](https://gitlab.aleph-alpha.de/research/attention-rollout/-/tree/master/examples/streamlit)
* [Original paper](https://arxiv.org/abs/2005.00928)
