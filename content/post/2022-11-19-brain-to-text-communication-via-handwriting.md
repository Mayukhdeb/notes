+++
title = "Brain to Text Communication via handwriting"
date = "2022-11-19"
author = "Mayukh Deb"
tags = ["paper"]
+++

The original paper can be found [here](https://www.nature.com/articles/s41586-021-03506-2).

The authors of this paper have made a BCI that decodes handwriting movements from neural activity and translates it to text using RNNs to decode signals. 

In one of the early experiments, they asked a paralysed subject to "attempt" to write as if his hand was not paralysed. These are the main insights from the experiment:
- they recorded neural activity and then used PCA to extract the top 3 axes with the highest variance.
- when they used t-SNE, it was also revealed that "characters which are written similarly are closer together"
- overall takeaway: even after years of paralysis, the neural representations of handwriting in the brain is strong enough to be useful in a BCI

## Further investigation on [another related paper](https://www.frontiersin.org/articles/10.3389/fnhum.2021.653659/full)

In this paper, they use LM-like models to deocde EEG data. They see that a single pre-trained generalised pretty well accross different subjects.

In the field of BCI, it has been generally seen that shallow NNs are more effective than their deeper counterparts. So we just train a new small NN for each user. Even though shallow NNs are good when trained on one person, it is seen that deeper NNs suck less when theyre trained on person A and tested on person B when compared to shallow NNs.

We might be able to exploit the tranferable nature of the first few layers of DNNs in BCI too.

The authors have developed a framework where arbitrary EEG segments are encoded as a seq of learned vectors. They basically made EEG -> Embeddings. Problems like sleep-stage classification involves smooth changes in the signals within the brain. White EEG data from other tasks might be different.

Notes on training the transformer:
1. They first train a transformer-encoder
2. They use a weight init scheme known as T-Fixup
3. 8 layers, with 8 heads, model dimension of 1536 and an internal feed-forward dimension of 3076
4. Represent position using an additive (grouped) conv layer
5. Cosine learning rate decay
6. Linear warm-up for 5 and 10% of total training steps (batches) for pre-training and fine-tuning
7. The pre-training procedure largely follows that of [wav2vec 2.0](https://pytorch.org/tutorials/intermediate/speech_recognition_pipeline_tutorial.html)

The total number of parameters trained in the final model was over one billion parameters.
