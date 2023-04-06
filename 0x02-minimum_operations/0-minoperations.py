#!/usr/bin/python3
"""Min operations challenge with python."""

def minOperations(n):
    """Min Operations calculation."""
    if n < 1:
        return 0
    if n == 1:
        return 0
    
    for i in range(n//2, 0, -1):
        if n % i == 0:
            
            return minOperations(i) + (n // i)
    
    return 0
