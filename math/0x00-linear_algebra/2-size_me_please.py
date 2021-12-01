#!/usr/bin/env python3
"""
Write a function def matrix_shape(matrix):that calculates the shape of matrix:

   You can assume all elements in the same dimension are of the same type/shape
   The shape should be returned as a list of integers

"""


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    shape_test = []
    while isinstance(matrix, list):
        shape_test.append(len(matrix))
        matrix = matrix[0]
    return shape_test
