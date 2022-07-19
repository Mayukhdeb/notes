+++
title = "Locating and Editing Factual Knowledge in GPTs"
date = "2022-07-19"
author = "Mayukh Deb"
tags = ["paper"]
+++

This paper's approach has been to develop a mechanism to identify the neuron activations that lead to a model's factual predictions and possibly even edit existing facts.

## Key concepts and takeaways:

### **What is a fact tuple?**

It is a special way to store knowledge in the form of  a tuple which looks like the following:

```python
## (subject, relation, object)
("Edmunt Neupert", "Plays the instrument", "Piano")
```

It contains the subject (index 0), the object (index 2) and their relation (index 1).

### **Knowing differs from saying**

Just because an LLM "knows" a fact, does not always mean that it'll state it in the completion. This is because transformers are pretty sensitive to the prompt itself.

Just how LLMs can **say** something without actually **knowing** it, it can also **know** something without **saying** it. 

### **What is knowledge in a LLM? If it exists, is there an elementary unit of knowledge within the models?**

**What if there was some specific computation within the LLM which plays a devcisive role for a given fact?**

It is fair to assume that a certain fact stored within the model is  evenly distributed among all of the computations being performed during the forward pass, but that is generally not the case. It turns out that when we corrupt the embeddings of certain input tokens, the probability of the original output changes drastically.

The question is, which part of the model and the prompt was responsible for this decisive change?

Let's try to understand this with an example:

```python

```

(WIP)