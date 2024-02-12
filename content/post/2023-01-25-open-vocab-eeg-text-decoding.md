The primary problem with most of the existing Brain-Signal to text pipelines is that they have a closed vocabulary. 

In this paper, they use pretrained language models for
EEG-To-Text decoding and make a zeroshot pilpieline for sentiment classification from EEG. The interesting part is that it can can leverage data from various subjects and sources, i.e huge potential for EEG to text systems with enough data.

Interesting quote from paper:

*The high-level idea is that we assume the human
brain to be a special kind of encoder, which functions similar to a language model that encodes a sequence of English tokens into contextualized embeddings*

I am primarily interested in the seq2seq model they managed to build from EEG data.

Important components that they used:
- word-level EEG features. (can be considered EEG "tokens"?)
- A multi layer transformer encoder to encode EEG features
- a pre-trained encoder-decoder BART model

They were able to successfully train a model for sentence reconstruction with cross entropy loss. The results are not amazing, but its proves that this direction of research is definitely worth pursuing.