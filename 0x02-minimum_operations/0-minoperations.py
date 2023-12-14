#!/usr/bin/python3
import sys
"""the minimum operation coding challenge """


def minOperations(n):

    num = 1
    operations = 0
    paste = 0

    while num < n:
        """ While my number of H are less than n """
        if n % num == 0:
            """ If my number of H are multiply of n, do Copy All and Paste"""
            paste = num
            num *= 2
            operations += 1
        else:
            """ If my number of H is not a multiply of n, do Paste only """
            num += paste
        operations += 1

    return operations
