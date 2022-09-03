+++
title = "Towards a New Science of Common Sense"
date = "2022-09-03"
author = "Mayukh Deb"
tags = ["paper"]
+++

## Intro

Common sense, as we know it has not yet been achieved in machines by any means despite decades of research. Today's large language models still struggle even the smallest of riddles or mental math questions. With LLMs, we have solved language, not logic/common sense.

AI is still very narrow. There are models which are "experts" at certain tasks, but none posess any general capabilities. AI as we know it today us super good at narrow domains like video games and image captioning. But they still struggle to solve simple riddles.

**Brittleness** - A known shortcoming of current AI systems is that they're very likely to fail to produce reasonable outcomes as soon as we provide it with an input slightly beyond it's boundaries. 

The word boundaries refers to the domain of data upon which it had learned. They generalise well, but only within the boundaries of it's own input data.

In simple words, they cannot handle unanticipated events.

Self driving cars do not offer reasons for their actions to the driver, and neither is it able to correct its behaviour by taking advice from the driver. It is a static, black box system. But what we need is a dynamic and intuitive system which can:
- provide explanations for it's actions
- learn with feedback from the driver on-the-fly

## Can we build a formal theory for common sense?

- Pat Hayes et.al developed a bunch of fancy rules ("axioms") which couldve worked as a baseline for common sense logic. 
- Marvin Minsky and Roger Schank proposed a model which was based on the memories of past experiences. The focus was less on getting conclusions, but more on recognizing patterns and building analogies between current events and remembered experiences

*"Knowing even a vast number
of commonsense facts is simply not the same as having and
exercising common sense in the real world"*

## What we can do

Instead of gobbling up GPUs with billions of parameters in models and datasets capturing trillions of tokens, we can try taking a step back.

A step back to understand what exactly common sense is. Some of the interesting questions we could ask are:

- How are experiences remembered, generalized, and organized so that they can be called to mind when needed?
- When should the model use it's world knowledge? or when should it stick to only the contextual info provided?

## Personal comments

LLMs are really just overpowered autocomplete machines. They're not super good at reasoning their way through even some of the simpler things. We need to re-think our approach to summoning basic common sense. With LLMs, we are solving language, not intelligence.

Language, when put together well sure does look like a sign of intelligence. But it is not. It is just valid syntax. Valid syntactical generators are good for open ended tasks like writing articles etc, but not for solving riddles.

We sure as hell need to look back and try to understand common sense. But who knows? perhaps scaling up LLMs is the answer after all. Only time will tell.