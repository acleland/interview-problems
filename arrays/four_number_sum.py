"""
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and 
an integer representing a target sum. The function should find all
quadruplets in the array that sum up to the target sum and return a
two-dimensional array of all these quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return
an empty array.
"""

def fourNumberSum(array, targetSum):
    ans = []
    numbers = { n: i for i, n in enumerate(array)}
    for idx1 in range(len(array) - 2):
        for idx2 in range(idx1 + 1, len(array) - 1):
            for idx3 in range(idx2 + 1, len(array)):
                n1, n2, n3 = array[idx1], array[idx2], array[idx3]
                complement = targetSum - n1 - n2 - n3
                if complement in numbers and numbers[complement] > idx3:
                    ans.append([n1, n2, n3, complement])
    return ans