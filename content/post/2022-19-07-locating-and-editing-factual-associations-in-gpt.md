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
prompt = "Miles Davis plays the"
```

Now on a normal GPT2-XL, the completion would be `piano` because Miles Davis was indeed a famous piano player.

The catch is, now when we "corrupt" the embeddings of the subject i.e `Miles` and `Davis`, then the output gets corrupted as well (i.e the probability of `piano` decreases)

**Side note: What do we mean by corrupting an input subject?**

The authors corrput the subject in the prompt by adding noise to the embeddings for all tokens in the prompt that refer to the subject entity (which in our case are 2 tokens `["Miles", "Davis"]`)

Since the input is now corrupted for some tokens along the seq dim, the hidden states of the model also get altered. In order to find which part(s) of the model was responsible for the original output (`piano`), we can now replace the specific "corrupted hidden states" with the original "clean hidden states" and see which combination leads to the highest probability of the original output.

(WIP)

## Resources

1. The paper (of course): https://arxiv.org/pdf/2202.05262.pdf
2. Website: https://rome.baulab.info/
3. Nice and elaborate walkthrough by the folks at Eleuther: https://www.youtube.com/watch?v=IkbYu_poZVE