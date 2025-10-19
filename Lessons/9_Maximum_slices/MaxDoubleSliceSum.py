# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 16:43:22 2025

@author: joche

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

# 100% solution
def solution(A):
    # Implement your solution here
    # Iterate through A, for every iteration add the current element a and compare this with the previous maximum slice.
    # This shifts Z by one for every iteration.
    # If the current value is lower than the previous Y value (the deleted value) or if the current value is lower than 0,
    # the X and Y position should be reevaluated.
    # 
    # If the current (new) value was lower than the previous lowest value:
    #   This should become the new delted (y) value. 
    #   The maximum single (default) slice will be the new double slice value.
    #   The single slice is defined as X-Z (so can be empty as the slice is X+1 - Z-1)
    # If the current (new) value was lower than 0:
    #   If the maximum single slice is larger than the double slice + the new value, then the new value will be the y value and the
    #   new double slice value will be the single slice value.
    
    N = len(A)
    y_val = A[1]
    max_dbl_end = 0 # X, Y, Z = 0, 1, 2 -> 1:2 but without 1 so nothing
    max_sin_end = max(A[1], 0)
    max_dbl_slice = max_dbl_end

    for a in A[2:N-1]:
        if a < y_val:
            max_dbl_end = max_sin_end
            y_val = a
        elif a < 0 and max_sin_end > max_dbl_end + a:
            max_dbl_end = max_sin_end
            y_val = a
        else:
            max_dbl_end += a

        max_sin_end = max(max_sin_end + a, 0)
        max_dbl_slice = max(max_dbl_slice, max_dbl_end)
    
    return max_dbl_slice