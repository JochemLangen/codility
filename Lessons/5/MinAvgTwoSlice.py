# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 23:28:26 2025

@author: joche

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

content_copy
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

content_copy
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

# Long solution by checking all slices
def solution(A):
    # Implement your solution here
    n = len(A)
    P = prefix_sums(A, n)
    min_avg = P[-1]/n
    min_ind = 0

    for i in range(0,n):
        for j in range(i+2,n+1):
            avg = (P[j] - P[i])/(j-i)
            if avg < min_avg:
                min_avg = avg
                min_ind = i
    return min_ind

def prefix_sums(A, n):
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

# However, every slice can be broken down into slices of 2 or 3 elements. 
# So we only need to find the smallest slice average of length 2 or 3.
# That is reflected below, though there is an even faster implementation possible 
# without going through pre-sums which is more like a*n instead of a*2n  

def solution(A):
    # Implement your solution here
    n = len(A)
    P = prefix_sums(A, n)
    min_avg = P[-1]/n
    min_ind = 0

    for i in range(0,n-2):
        avg = min((P[i+2] - P[i])/2, (P[i+3] - P[i])/3)
        if avg < min_avg:
            min_avg = avg
            min_ind = i

    avg = (P[n] - P[n-2])/2
    if avg < min_avg:
        min_avg = avg
        min_ind = n-2
    return min_ind

def prefix_sums(A, n):
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

# def min_dbl_slice(A,n):
#     total_min_dbl = A[0] + A[1]
#     min_k = 0

#     for k in range(2,n):
#         min_dbl = A[k-1] + A[k]

#         if min_dbl < total_min_dbl:
#             total_min_dbl = min_dbl
#             min_k = k-1
#     return min_k

print(solution([1,2,3,4,5]))