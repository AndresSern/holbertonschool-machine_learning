#!/usr/bin/env python3
"""
Defines a function that creates the forward propagation graph
for the neural network
"""


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates the forward propagation graph for the neural network
    parameters:
        x [tf.placeholder]: placeholder for input data
        layer_size [list]: contains number of nodes in each layer of network
        activations [list]: contains activation functions for each layer
    returns:
        prediction of the network in tensor form
    """
    first_layer = create_layer(x, layer_sizes[0], activations[0])
    last_layer = first_layer
    for layer in range(1, len(layer_sizes)):
        last_layer = create_layer(last_layer, layer_sizes[layer],
                                  activations[layer])
    return last_layer
