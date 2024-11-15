#!/usr/bin/python3

def minOperations(n):
    """
    Method to calculate the minimum number of operations
    required to result in exactly n 'H' characters
    using the operations: Copy All and Paste.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
