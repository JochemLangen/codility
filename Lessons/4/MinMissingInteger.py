# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 22:37:23 2025

@author: joche

This is a demo task.

Write a function:

def solution(A)
content_copy

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

def solution(A):
    # Implement your solution here
    count = counting(A, 1000000)

    for i, j in enumerate(count):
        if j == 0:
            return i+1
    pass

def counting(A, m):
    n = len(A)
    count = [0] * m 
    for k in range(n):
        if A[k] > 0:
            count[A[k]-1] += 1
    return count

# 100% score

solution([100000])