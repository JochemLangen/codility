# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 17:15:47 2025

@author: joche

A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
"""

import math

# 93%, one test was too slow (1.25 instead of 0.84 seconds)
def solution(A):
    # Implement your solution here
    # First find the indices of all the peaks -> O(n)
    # For n peaks found, loop through the no. of flags from n to 1 and stop if one of them meets the distance criteria
    #
    # To see if it meets the criteria:
    #   For every peak could loop through all the other peaks and write down the distances.A
    #   Then for every n, check the combinations allowed - still have subsequent complexity and O(n^2) at least
    # Or:
    #   Check how many times n fits in each peak. 
    #   From the peak value you subtract the position of the last unique peak 
    #   The number peaks for which (peak - last val) // n == 1 is the number of valid flags (which must be equal to n).
    #   Variant:
    #   Can check in every loop if n_peak - i + valid < n (then it is already a fail) or valid >= n (already a success)

    ff = flag_finder(A)

    ff.find_peak()

    return ff.max_flag()

class flag_finder():    

    def __init__(self, A):
        self.A = A
        self.N = len(A)
        self.n_peak = 0
        return

    def find_peak(self):
        A = self.A
        N = self.N
        peaks = [0]*N
        n_peak = 0

        if N > 2:
            i = 1
            while i < N-1:
                if A[i] > A[i-1] and A[i] > A[i+1]:
                    peaks[n_peak] = i
                    n_peak += 1
                    i += 2
                else:
                    i += 1
            self.peaks = peaks[:n_peak]
            self.n_peak = n_peak
        else:
            self.peaks = []
            self.n_peak = 0
        return

    def max_flag(self):
        n_peak = self.n_peak
        peaks = self.peaks
        flags = 0

        for n in range(
            min(n_peak, math.floor(math.sqrt(self.N))),
            0,-1):

            flags = 1
            prev_peak = peaks[0]
            for i in range(1,n):
                if (peaks[i] - prev_peak) // n > 0:
                    flags += 1
                    prev_peak = peaks[i]
                elif n_peak - i-1 < n - flags:
                    break

            # Separate for loops such that the flags == n logic does not need to be 
            # gone through as much
            for i in range(n,n_peak):
                if (peaks[i] - prev_peak) // n > 0:
                    flags += 1
                    prev_peak = peaks[i]

                    if flags == n:
                        return n
                elif n_peak - i-1 < n - flags:
                    break
        return flags
        