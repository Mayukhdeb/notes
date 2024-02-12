When compared to artificial neural networks, the human brain is a lot more modular. The authors believe that this is because the loss function of ANN regularizers like weight decay are not dependent on the permutations of neurons on each layer.

The cost of connecting 2 biological neurons which are far apart is much more than when they're closer together. But this is not the case for ANNs.

In order to impose a similar phenomenon to that of brains, the authors propose the following steps:

1. Embed every neuron in a model into a 2D space where x = neuron index and y layer index
2.  Augment the loss function with a cost proportional to the length
of each neuron connection times the absolute value of the connection weight

Number 2 aims to keep neurons that need to communicate as close together as possible

<!-- 
I think we can also apply this method to LLM training to see if we get simple circuits as a emergent behaviour during training.
 -->

### Weight layers vs neuron layers

There is a difference between weight layers and neuron layers.

```python
import torch.nn as nn

model = nn.Sequential(
    ## ...there can be more layers over here
    # neuron layer with 10 neurons
    nn.Linear(10, 7),              ## weight layer
    # neuron layer with 7 neurons
    nn.Linear(7, 5),               ## weight layer
    # neuron layer with 5 neurons
    nn.Linear(5,3)                 ## weight layer
    # neuron layer with 3 neurons
)
```

* **Weight layers**: actual `nn.Linear` modules. Where `num_inputs` and `num_outputs` are the number of neurons incoming and outgoing from a single layer. A model with `L` linear layers -> there are `L` weight layers

* **Neuron Layers**: The neuron layers are basically the outputs of each layer.

### Representing weights in 2D space

In order to represent distance in between each neuron in each layer. We arrange all neurons in a 2D plane such that `x` refers to the neuron index and `y` refers to the layer index.

* Every neuron in the same layer would have the same y co-ordinate, but different x co-ordinate. Neurons are seperated from each other uniformly horizontally.
* Layers in different neurons have different y co-ordinates.

## Defining the spatial relation in between neurons

In between the neuron layers, lies a weight layer with weights `W`.

This layer contains a matrix of size `(num_input_neurons, num_output_neurons)`.

Let us imagine a simple pytorch model:



The weight that connects neuron index 4 of first neuron layer to the neuron index 2 of the 2nd neuron layer is: `W[4, 2]`

Given 2 neurons `n1: (x1, y1)` and `n2: (x2, y2)` where `(x,y)` is the position of the neurons in 2D space, the distance between them can either be the L1 distance or the L2 Norm.

* L1: `abs(x1 - x2) + abs(y1 - y2)`
* L2: `(x1 - x2)**2 + (y1 - y2)**2`

## Localization to encourage locality

WIP