+++
title = "Language Models (mostly) Know What they know"
date = "2022-07-14"
author = "Mayukh Deb"
tags = ["paper"]
+++

# Can we make LMs predict which questions they'll be able to answer correctly?

It is important for LLMs to "know" what they know and what they do not know. The problem is that LMs are generally never trained to say "I do not know". But it might be possible to quantify this ability post-training.

This is how they approach the problem:

1. Finetune models with a value head to predict the probabiility that they can answer a given question correctly.
2. Verify if the answwers provided by the LM corresponds to certain sources/hints (hints could be correct or wrong)


**Some terminology**

1. `P(IK)`:  probabiility that the LM can answer a given question correctly
2. `P(True)`: probability that the model assigns to the fact that it answered a given question correctly.

# Obervations:

1. **What are "harder" questions?**

They're the questions which are less likely to be contained in the world knowledge of the model. Even if they are contained, there would be many possible "right" answers to it. For example: *"What is the name of Daniel's mother?"* is a harder question than *"Who is the Chancellor of Germany?"* simply because the first question's answer could basically be any name, while the 2nd question only has one valid answer that the model has probably already "seen" many times during training.

2. **Token sequences which ask "harder questions" have lower `P(IK)` scores on the last few questions**

My personal belief is that this is in the very nature of how transformers work. Transformers are autocomplete machines. For questions where the model already knows the answer from world knowledge, it tends to basically get into the flow through the last few tokens before throwing out the answer. 

3. **Asking models if the given answer is `True` or `False`**

 The approach is surprisinglty simple, it's pretty much just prompt engineering:

This is how the prompt looks like:
 ```
Question: Who was the first president of the United States?
Proposed Answer: George Washington
Is the proposed answer:
(A) True
(B) False
The proposed answer is:
 ```

3. **Asking models if their own answers are `True` or `False`**

This is yet again done with prompt engineering in 2 stages:

First, we sample an answer from the model:
```
Question: Who was the first president of the United States?
Answer:
```

Then, we ask the model about it's own answer:

```
Question: Who was the first president of the United States?
Proposed Answer: George Washington was the first president.
Is the proposed answer:
(A) True
(B) False
The proposed answer is:
```

4. **On "hard questions", LMs are far more confident about the "correctness" of their answer if we provide contextual information**

For example, let us consider an obscure question which is very likely to not be contained in the model's world knowledge:

```
What state’s rodeo hall of fame was established in 2013?
```

The `P(IK)` for this question is 18%, which is pretty low. However, if we prepend a wikipedia article on the Idaho Rodeo Hall of Fame on the prompt, then the `P(IK)` jumps to 78%. In simple words, the model is far more confident that it can answer an unseen question correctly if we provide it some context. 

```
Wikipedia: The Idaho Rodeo Hall of Fame was established as a 501 (c)(3) nonprofit organization on May 6, 2013. Lonnie and Charmy LeaVell are thefounders of the organization. The actual charitable nonprofit status was...
<CROPPED>
What state’s rodeo hall of fame was established in 2013?
```

# Closing comments

All of us are trying to understand and validate the factual accuracy of the answers we obtain from LLMs. It is indeed an interesting approach to use the model itself to try and validate it's own answers, but I'm still skeptical. It's like asking "are you sure?" to a guy you already don't trust as a mechanism to get reliable answers.

Kind of reminds me of the "Let's think step by step" trick, but now it's more like "Is the given answer correct?".