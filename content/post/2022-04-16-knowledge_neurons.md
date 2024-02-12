# Knowledge Neurons

The knowledge neurons paper asks the following question: 

*Given an output `y` from an intermediate layer, how can we determine the neurons which contributed the most/least to the prediction ?*

The neurons which contribute the most to the "fact" mentioned by the model are generally tagged as the "*knowledge neurons*". 

## Procedure to find knowledge neurons 

1. Produce `n` different and diverse prompts expressing this fact 

2. For each prompt, calculate the attribution score of each intermediate neurons

3. For each prompt, set an attribution score threshold `t` and retain only neurons with attribution scores greater than `t`, which are coarse knowledge neurons 

4. We design our knowledge attribution method based on integrated gradients to evaluate the true contribution of each specific intermediate neuron in FFNs (Feed Forward Networks) to the final output.

5. Considering coarse knowledge neurons of all prompts, set a sharing percentage threshold and retain only neurons shared by more than prompts. The finally retained neurons are true knowledge neurons, where the fact is located.


## Drawbacks:

1. Generally this method **does not work well with a single input prompt**. It needs multiple sentences which have the same meaning but written differently in order to work effectively. Much like augmenting images in gradcam/IntegratedGradients to generate smoother heatmaps.  One interesting way to possibly fix this issue would be to use something like NoiseGrad in the layers to get smoother outputs with a smaller amount of alt sentences. 

2. Another drawback is the fact that is a **localised explanation method**, which can encapsulate only a small part of the model at a given instance. We can potentially find a way to find an extended "knowledge neuron map" which spans though multiple layers of the model. 

## Other interesting facts:

* Suppressing and amplifying knowledge neurons can control the expressions of the corresponding knowledge, without affecting other facts.

* Such knowledge surgery in pretrained Transformers enables us to update incorrect knowledge, and to erase unethical knowledge.

<!-- # What can I try out ? 

- figure out how to implement knowledge neurons in gpt 2 colab -- maybe look into knowledge neurons eleuther source code ? 
- what happens if we use noisegrad along with integrated gradients while looking for knowledge neurons ? 
- how do knowledge neurons from one layer "talk to" the knowledge neurons in the next layer ?
- can we "see" knowledge being extracted and passed from one layer to another ?
- attribute knowledge neurons from layer i+1 to knowledge neurons of layer i.  -->

## Resources:
- [The original paper on arxiv](https://arxiv.org/abs/2104.08696)
- [Intro to integrated gradients](https://blog.fiddler.ai/2020/04/video-ai-explained-what-are-integrated-gradients/) Nice warm-up article explaining how integrated gradients work and why they make sense.
- [EleutherAI/knowledge-neurons](https://github.com/EleutherAI/knowledge-neurons) a python library where they implemented the method for some transformers.
