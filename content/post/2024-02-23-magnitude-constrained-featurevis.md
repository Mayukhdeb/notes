The primary drawback of feature visualization has been it's inability generate interpretable features in deeper networks. In my own experience, I've seen that feature vis basically stops working once we go past the 3rd resnet block on a resnet18.

This paper fixes this issue by optimizing the images in the phase spectrum while keeping the magnitude constant. I have explained the concept of a phase spectrum in this [other post](https://mayukhdeb.github.io/notes/posts/2024-02-24-phase-spectrum.html).

---

There are 2 main approaches for feature visualization:

1. Gradient ascent with a penalty for high frequencies in the fourier domain. Combined with data augmentation.
2. Gradient ascent on a subspace parameterized by a generative model.

The first method fails on large/deep models. The 2nd method is not very useful since it's dependent on the generative model's own biases. The only way forward is to understand why method 1 fails for deeper models.

Unlike shallow models like VGG etc, running featurevis on deeper models yield higher frequency components which are impossible to interpret by humans. To illustrate this, they ran featurevis on the logits of a ViT trained on imagenet and compared it's mean power spectrum (left) with that of the Imagenet dataset's power spectrum (right).

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/c2c0133f-4e60-4eea-ace6-cad344176aaf" width = "80%">

This proves that featurevis images contain a a much larger amount of high frequency components. The solution to this problem would be to constrain the power spectrum to lower frequency components only.

Apart from constraining high frequencies, the method is also motivated by psychophysics experiments [1, 2] that have shown that  when viewing images, humans are more sensitive to differences in phase than in magnitude. The authors build an analogous mathematical constraint for featurevis which optimizes only the phase of the image and not the magnitudes of the frequency components. 

# Method

The first thing that they do is that they break down the fourier spectrum into magnitude and [phase spectrum](https://mayukhdeb.github.io/notes/posts/2024-02-24-phase-spectrum.html). They optimize the phase spectrum of the image while keeping the magnitude spectrum to a constant at an average value computed over a set of natural images.

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/4419c6be-da5a-474d-95ae-9aaa9a6b82ab" width = "100%">

On a side note, this method also reduces the number of trainable parameters by half.

---

# References

[1] - [Image phase or amplitude? Rapid scene categorization is an amplitude-based process](https://comptes-rendus.academie-sciences.fr/biologies/articles/10.1016/j.crvi.2004.02.006/)

[2] - [On the role of spatial phase and phase correlation in vision, illusion, and cognition](https://www.frontiersin.org/articles/10.3389/fncom.2015.00045/full)