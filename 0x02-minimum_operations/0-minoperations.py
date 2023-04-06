#!/usr/bin/python3
'''Minimum Operations Challenge'''


def minOperations(n):
    '''Calculated fewest number of operations.
        Integer : if n is not achieveable, return 0
    '''
    pasted = 1
    copied = 0
    cnter = 0

    while pasted < n:
        if copied == 0:
            copied = pasted
            cnter += 1

        if pasted == 1:
            pasted += copied
            cnter += 1
            continue

        remaining = n - pasted
        if remaining < copied:
            return 0

        if remaining % pasted != 0:
            pasted += copied
            cnter += 1
        else:
            
            copied = pasted
            
            pasted += copied
            
            cnter += 2

   
    if pasted == n:
        return cnter
    else:
        return 0
