# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 20:32:08 2025

@author: joche

You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
"""

def simple_solution(A):
    # Simple O(N^2) solution
    N = len(A)
    count = [0]*N
    for i, a in enumerate(A):
        for b in A:
            if a % b != 0:
                count[i] += 1
    return count

# 100% solution at most O(2*N * (1 + log(2*N))) so O(N * log(N))
def solution(A):
    # Way to count without
    N = len(A)
    occ, max_val = count_occ(A) # O(N)
    nondiv = [N-1]*(max_val + 1)
    
    for i in range(1, max_val+1): # The outer loop is at most O(2*N) so total loop
                                  # is at most O(2*N * log(2*N))
        if occ[i] > 0:
            nondiv[i] -= (occ[i] - 1) # Remove its own entries

            # Remove its entries from its multiples
            k = i * 2
            while k <= max_val: # At most O(log(2*N))
                nondiv[k] -= occ[i]
                k += i
        else:
            continue
    count = [0]*N

    for i, a in enumerate(A): # O(N)
        count[i] = nondiv[a]

    return count

# def solution(A):
#     # Implement your solution here
#     # Could count the occurences of every value and list the non-divisors using the sieve.
#     # Finally multiply these together as np arrays. Counting occurences will a fair lot of 
#     # memory (time will be O(3N) and the sieve will take ~O(N) but per non-zero element in occ so O(N^2). Could be ok
#     #
#     # Simple solution is also O(N^2)
#     N = len(A)
#     count = count_occ(A)

#     for 

#     pass

def count_occ(A):
    N = len(A)
    max_val = max(A)
    count = [0]*(max_val + 1)
    for a in A:
        count[a] += 1
    return count, max_val