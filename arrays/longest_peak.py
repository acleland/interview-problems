"""
Longest Peak

Write a function that takes in an array of integers and returns the length
of the longest peak in the array.

A peak is defined as adjacent integers in the array that strictly increasing
until they reach a tip (the highest value in the peak), at which point, they
become strictly decreasing. At least three integers are required to form a peak.
"""


def longestPeak(array):
    maxPeak = 0
    currentPeak = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            currentPeak = 3
            j = i - 1
            while j > 0 and array[j] > array[j-1]:
                currentPeak += 1
                j -= 1
            j = i + 1
            while j < len(array) - 1 and array[j] > array[j + 1]:
                currentPeak += 1
                j += 1
            maxPeak = max(currentPeak, maxPeak)
    return maxPeak