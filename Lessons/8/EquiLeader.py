# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 22:18:44 2025

@author: joche

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""


# The solution at the bottom is correct but slow instead consider the following:
# If you slice A in x number of slices, there is only an equi leader if there is the
# same leader in all slices. To be the leader in all slices the value must also
# be the leader in the main array. 
# So you once have to find the leader of the main array and then loop through the indices
# counting the number of occurences in the left and right slice and checking it is therefore 
# still a leader in both

# 100% solution
#
def solution(A):
    # Implement your solution here
    N = len(A)
    count = 0
    no_leader, candidate, occ = find_leader(A, N)
    if no_leader:
        return 0

    occ_left = 0
    occ_right = occ
    for i, val in enumerate(A):
        if val == candidate:
            occ_left += 1
            occ_right -= 1
        
        leader_left = occ_left > (i+1)//2
        leader_right = occ_right > (N-i-1)//2
        if leader_left and leader_right:
            count += 1
    
    return count

def find_leader(A, N):

    size = 0
    for a in A:
        if size == 0:
            size = 1
            value = a
        elif a != value:
            size -= 1
        else:
            size += 1
    if size > 0:
        found, count = verify_candidate(A, N, value)
        if found: 
            return False, value, count
    
    return True, 0, 0

def verify_candidate(A, N, candidate):
    count = 0
    for a in A:
        if a == candidate:
            count += 1

    if count > N//2:
        return True, count
    else:
        return False, 0
    
# Slower solution

def slow_solution(A):
    # Implement your solution here
    # Loop through all splitting indices. Find the leader of the smallest side and use that as a candidate for the other.
    N = len(A)
    count = 0

    for i in range(N//2):
        candidate, found = sl_find_leader(A[0:i+1])
        print('a',i, candidate, found, A[i+1:N], N-i-1)
        if found and sl_verify_candidate(A[i+1:N], N-i-1, candidate):
            count += 1

    for i in range(N//2,N-1):
        candidate, found = sl_find_leader(A[i+1:N])
        print('b', i, candidate, found, A[0:i+1], i+1)
        if found and sl_verify_candidate(A[0:i+1], i+1, candidate):
            count += 1
    return count

def sl_find_leader(A):

    N = len(A)
    size = 0
    for a in A:
        if size == 0:
            size = 1
            value = a
        elif a != value:
            size -= 1
        else:
            size += 1
    if size > 0 and sl_verify_candidate(A, N, value):
        return value, True
    else:
        return 0, False

def sl_verify_candidate(A, N, candidate):
    count = 0
    # n = N//2
    for a in A:
        if a == candidate:
            count += 1
            # if count > n:
                # return True
    # return False
    if count > N//2:
        return True
    else:
        return False