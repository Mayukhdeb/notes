+++
title = "Brain2Image: Converting Brain Signals into Images"
date = "2023-01-25"
author = "Mayukh Deb"
tags = ["paper"]
+++

**Can we encode useful visual information about images from the brain's EEG signals?**

Yes. Image generation from a brain signal feature vector encoding
information about visual classes is the main contribution of
this paper

---

The authors built an LSTM based generative method which learns a more compact and noise free version of the EEG data and uses it to generate visual stimuli evoking specific brain responses.

<!-- 
Can we replace the LSTM with an autoregressive transformer?
 -->

EEG contains patterns related to visual content which can be used to generate images which are effective at evoking visual stimuli. Their primary objective in this paper was:


Image (x) -> human brain -> EEG signals -> Brain2Image -> decoded image (y)


There are 3 main steps to this:

1. **data collection**: human looks at images on a screen and his brain signals are recorded
2. **feature extraction**: recorded EEG signals are passed through an encoder which returns a feature vector containing class discriminative information. 
3. **training image generators**: VAE decoders/GANs are trained on image-encoded signal pairs

## Learning the Latent space using LSTMs

Given an image stimulus, they feed the EEG time-series data into an LSTM + encoder which is trained to return class-discriminative feature vectors. This gave them over 80% classification accuracy.

I personally think that using a classification output would not be good for a latent vector since it was probably trained on a Cross Entropy-like loss where the outputs of 2 different classes (even if theyre visually similar) would have very low cosine similarity. This way, the vector space would be skewed quite a bit and hence not be suitable for latent vector interpolations etc.

## Leveraging the latent space to generate images

The authors tried 2 main approaches:
1. VAEs
2. GANs

For the GAN training, they used 100 dimensional random noise (`z`) and 128 dimensional EEG features.

Overall, the GAN approach seems to be a better performer in terms of inception scores and inception classification accuracy. Even to my eyes they seemed better.

