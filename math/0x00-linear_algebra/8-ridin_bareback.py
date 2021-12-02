#!/usr/bin/env python3
"""
Write a function def mat_mul(mat1, mat2): that performs matrix multiplication:

  You can assume that mat1 and mat2 are 2D matrices containing ints/floats
  You can assume all elements in the same dimension are of the same type/shape
  You must return a new matrix
  If the two matrices cannot be multiplied, return None
"""


def mat_mul(mat1, mat2):
    """ Function that performs matrix multiplication """
    if len(mat1[0]) == len(mat2):
        mat_mul = []
        for r_mat1 in mat1:
            temp_array = []
            for r_mat2 in zip(*mat2):
                result = sum([v_1 * v_2 for v_1, v_2 in zip(r_mat1, r_mat2)])
                temp_array.append(result)
            mat_mul.append(temp_array)
        return mat_mul
    return None
