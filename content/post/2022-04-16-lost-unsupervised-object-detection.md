+++
title = "LOST - Localizing objects with self supervised transformers"
author = "Mayukh Deb"
tags = ["paper"]
date = "2022-04-16"
+++


# Lost - Localizing objects with self supervised transformers and no labels

The core idea is to be able to use the hidden info within transformers to localize objects ("subjects") within input images (much like a YOLO model but without further training). 

## How does it work ?

1. First, we assume that there's at least one object to be found in the image.

2. it relies on a selection of patches that are likely to belong to an object. We call these patches “seeds.

**What are these seeds ?**

We select a seed based on the assumptions that:
* regions/patches within objects correlate more with each other than with background patches
* an individual object covers less area than the background

We should also know that patches in an object correlate positively with each other but negatively to the background patches.

3. We pick the first seed by picking the patch with the smallest number of positive correlations with the other patches.

4. We then build a patch similarity matrix which says how similar each patch is to every other patch.

5. The next step is to find the next patches which are also likely to fall into the object. We do this by relying on the fact that pixels within an object tend to be positively related.

6. We keep expanding using this rule for as long as there are patches which are positively correlated to the seed patch.

7. Finally, we draw a bounding box around the final patch.

## CAD

* CAD (Class Agnostic Detection): Localizes objects in an image regardless of its semantic category. Basically there would be 2 categories, foreground and background.

## Limitations

* Cannot seperate same classes instances which overlap.
* Does not work well when the object covers a large portion of the image.

## Resources
The implementation can be found [here](https://github.com/valeoai/LOST).
