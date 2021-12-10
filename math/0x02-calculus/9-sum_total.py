#!/usr/bin/env python3
"""
Write a function def summation_i_squared(n): that calculates a sigma to the
  square
    n is the stopping condition
    Return the integer value of the sum
    If n is not a valid number, return None
    You are not allowed to use any loops
"""


def summation_i_squared(n):
    """ that calculates a sigma to the square """
    print("inside function")
    multiply = n * (n + 1) * (2 * n + 1)
    return multiply // 6
