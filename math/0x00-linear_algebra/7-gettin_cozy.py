#!/usr/bin/env python3
"""
Write a function def cat_matrices2D(mat1, mat2, axis=0):
    that concatenates two matrices along a specific axis:

  You can assume that mat1 and mat2 are 2D matrices containing ints/floats
  You can assume all elements in the same dimension are of the same type/shape
  You must return a new matrix
  if the two matrices cannot be concatenated, return None
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """ Function that concatenates two matrices along a specific axis """
    if axis == 0:
        if len(mat2[0]) == len(mat1[0]):
            copy_mat1 = mat1.copy()
            test_mat1 = mat1.copy() + ([*mat2])
            for row2 in mat2.copy():
                copy_mat1 = copy_mat1 + [row2]
            return test_mat1
        return None
    elif axis == 1:
        if len(mat2) == len(mat1):
            return [row_1 + row_2 for row_1, row_2 in zip(mat1, mat2)]
        return None
