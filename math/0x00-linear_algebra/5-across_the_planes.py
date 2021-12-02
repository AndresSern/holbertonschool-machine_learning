#!/usr/bin/env python3
""" Write a function def add_matrices2D(mat1, mat2):
    that adds two matrices element-wise:

  You can assume that mat1 and mat2 are 2D matrices containing ints/floats
  You can assume all elements in the same dimension are of the same type/shape
  You must return a new matrix
  If mat1 and mat2 are not the same shape, return None
"""


def add_matrices2D(mat1, mat2):
    """Function that adds two matrices element-wise"""
    if len(mat1) == len(mat2):
        new_matrix = []
        for row_1, row_2 in zip(mat1, mat2):
            if len(row_1) == len(row_2):
                temp = []
                for value_1, value_2 in zip(row_1, row_2):
                    temp.append(value_1 + value_2)
                new_matrix.append(temp)
            else:
                return None
        return new_matrix
    return None
