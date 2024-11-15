#!/usr/bin/python3
""" Minimum Operations
"""

def min_operations(n: int) -> int:
    """Minimum operations needed to get n H characters"""
    next_char = 'H'
    body = 'H'
    operations = 0

    while len(body) < n:
        if n % len(body) == 0:
            operations += 2
            next_char = body
            body += body
        else:
            operations += 1
            body += next_char

    if len(body) != n:
        return 0

    return operations
