"""
Zero Sum Subarray

You're given a list of integers nums. Write a function that returns a boolean
representing whether there exists a zero-sum subarray of nums. 

A zero-sum subarray is any subarray where all of the values add up to zero. A
subarray is any contiguous section of the array. For the purposes of this problem,
a subarray can be as small as one element and as long as the original array.
"""

def zeroSumSubarray(nums):
    # Write your code here.
    sums = set()
    sum = 0
    for n in nums:
        sum += n
        if sum in sums or sum == 0:
            return True
        else:
            sums.add(sum)
    return False