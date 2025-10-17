# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 21:39:17 2025

@author: joche

You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
"""
#100% solution
def solution(H):
    # Implement your solution here
    # Stack that adds when the next entry in H is higher than the previous and pops if it is lower until the block
    # at the top of the stack is the same height or lower. If it is lower a new block will be stacked on top to get to the desired height.
    # Every stack is a block
    n = 0
    N = len(H)
    stack = [0]*(N+1)
    stack_head = 0
    i = 0
    while i < N:
        if H[i] > stack[stack_head]:
            stack_head += 1
            stack[stack_head] = H[i]
            n += 1
            i += 1
        elif H[i] == stack[stack_head]:
            i += 1
        else:
            stack_head -= 1

    return n