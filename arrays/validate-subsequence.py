"""
Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the 
second array is a subsequence of the first.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array
but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4]
form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single
number in an array and the array itself are both valid subsequences of the array.

~~~
"""

def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    for n in array:
        if n == sequence[i]:
            i += 1
            if i >= len(sequence):
                return True
    return False
