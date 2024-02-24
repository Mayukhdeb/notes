The primary drawback of feature visualization has been it's inability generate interpretable features in deeper networks. In my own experience, I've seen that feature vis basically stops working once we go past the 3rd resnet block in a resnet18.

This paper somehow fixes this issue by optimizing the images in the phase spectrum while keeping the magnitude constant.

**What is the phase spectrum?**

We know that the fourier transform provides the frequency domain information about the signal. The phase spectrum provides the individual phases of each individual frequency component in the frequency domain representation. To gain a better understanding, let's visualize it in a few plots.

