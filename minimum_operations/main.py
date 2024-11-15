#!/usr/bin/python3
"""
Main file for testing
"""

min_operations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, min_operations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, min_operations(n)))
