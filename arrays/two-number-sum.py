"""
Two Number Sum 

Write a function that takes a non-empty array of distinct integers and an integer target
sum. If any two numbers in the input array sum up to the target sum, the function should
return them in an array, in any order. If no two numbers sum up to the target sum,
the function should return an empty array.

You can assume that there will be at most one pair of numbers summing up to the target sum.
~~~
"""

def twoNumberSum(array, targetSum):
    # Write your code here.
	visited = set()
	for n in array:
		complement = targetSum - n
		if complement in visited:
			return [n, complement]
		visited.add(n)
	return []

