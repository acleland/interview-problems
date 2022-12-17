"""
Monotonic Array

An array is said to be monotonic if it is either nonincreasing or nondecreasing from left to right. 

Write a function that takes an array and returns a boolean determining if the array is monotonic.

"""

def isMonotonic(array):
    # Write your code here.
    nondecreasing = True
    nonincreasing = True
    for i in range(len(array) - 1):
        if array[i + 1] > array[i]:
            nonincreasing = False
        elif array[i + 1] < array[i]:
            nondecreasing = False
        if not (nondecreasing or nonincreasing):
            return False
    return True