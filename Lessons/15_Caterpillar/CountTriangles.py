# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 23:28:04 2025

@author: joche

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

def solution(A):
    # Implement your solution here
    # Three index caterpillar algorithm, moving P, Q, R through the array after sorting it.
    A.sort()
    N = len(A)
    tri = 0

    for P in range(0,N-2):
        R = P + 2
        for Q in range(P+1, N-1):
            while R < N and A[P] + A[Q] > A[R]:
                R += 1
            tri += R - Q -1
    return tri