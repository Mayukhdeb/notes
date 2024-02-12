I will start by rambling a little about how [learning language is harder than you think](https://garymarcus.substack.com/p/learning-language-is-harder-than). Then I'll move on to the main paper itself.

## Learning language is harder than you think

An interesting point that was made in the article was that a language is learned *not* entirely through memorization. Sentences like *I breaked the window* are grammatically invalid, but they still manage to get the meaning accross. We manage to make a meaningful fact tuple i.e `({person}, break, window)`. And the sentence *I breaked the window* is just a crude way to imply that exactly that.

LLMs like that of GPT-3 are really good at generating text which looks "realistic". But they face the problem that DALLE-2 faces with compositionality.

The reasons as to why DALLE-2 cannot consistently make an image of a red box on a blue box might just be the same as to why GPT-3 cannot stuff like logical reasoning (sure it can solve small riddles, but what about longer chains of thought?).

Another important point that was made was that children require far less amount of "training data" when compared to that of LLMs to pick up their language.

*"To date, nobody, ever, has given a convincing and thorough account of how human children (and human children alone) learn language. To get there, You would probably want a rich theory about how people represent meanings"*

The way we train LLMs today basically follows this principle: *"Let's throw in as many words as possible into the neural net and make it predict the next one in hopes that this will somehow make it smart."*

My personal opinion is that these LLMs are just really really good clever hanses. They are very good at being grammatically fluent, but that does not imply that they're a good model for the human mind. They are like very good parrots, knowing how to arrange words in the right order, but never to actually understand them.

GPTs do not tell us things about the world, it simply imitates the patterns of human language. It has no form of reasoning built into it.

## The Third wave

The solution to some of the drawbacks of current deep-learning method might just emerge from something called "Neurosymbolic AI". 

**What is neurosymbolic AI?**

It is an alternative approach to build systems which not just classify/predict certain variables, but also have some sort of an internal mechanism of logical reasoning. It's a way to make neural networks "think step by step" so that they generalise with lower amounts of data.

**AI cookbook**

Gary Marcus proposes that we should build a system that can acquire, represent, and manipulate abstract knowledge.

In order to be actually smart, AGI would require a form of symbolic manipulation of variables in logic.
