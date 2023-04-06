#!/usr/bin/python3
"""Min operations challenge with python."""

def minOperations(n):
    """
    Min Operations calculation
    """
    if n < 1:
        return 0
    if n == 1:
        return 0
    # Find the largest factor of n
    for i in range(n//2, 0, -1):
        if n % i == 0:
            # Recursively calculate the number of operations needed
            return minOperations(i) + (n // i)
    # If no factors are found, n is prime and cannot be achieved
    return 0
