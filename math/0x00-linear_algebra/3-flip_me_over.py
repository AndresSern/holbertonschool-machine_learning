#!/usr/bin/env python3
"""
Write a function def matrix_transpose(matrix): that returns
the transpose of a 2D matrix, matrix:

  You must return a new matrix
  You can assume that matrix is never empty
  You can assume all elements in the same dimension are of the same type/shape

"""


def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]
