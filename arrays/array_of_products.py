"""
Array of Products

Write a function that takes in a non-empty array of tegers and returns an array
of the same length, where each element of the output array is equal to the product
of every other number in the array.

In other words, the value at output[i] is equal to the product of every number in
the input array other than input[i]

Implement this problem without using division
"""


def arrayOfProducts(array):
    output = [0 for _ in range(len(array))]
    productUpTo = {}
    productAfter = {}
    product = 1
    for i in range(len(array)):
        productUpTo[i] = product
        product *= array[i]
    product = 1
    for i in reversed(range(len(array))):
        productAfter[i] = product
        product *= array[i]
    for i in range(len(array)):
        output[i] = productUpTo[i] * productAfter[i]
    return output
        
     