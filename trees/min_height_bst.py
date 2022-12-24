"""
Min Height BST

Write a function that takes in a non-empty sorted array of distinct integers,
constructs a BST from the integers, and returns the root of the BST.

The function should minimize the height of the BST.

[1, 2, 5, 7, 10, 13, 14, 15, 22           

              10
             /
            2
           / \
          1   5
"""

def buildBST(bst, array, start, end):
    if end < start:
        return bst
    mid = start + (end - start)//2
    bst.insert(array[mid])
    print(array[mid])
    buildBST(bst, array, start, mid - 1)
    buildBST(bst, array, mid + 1, end)
    return bst
    

def minHeightBst(array):
    start = 0
    end = len(array) - 1
    mid = end // 2
    bst = BST(array[mid])
    buildBST(bst, array, start, mid - 1)
    buildBST(bst, array, mid + 1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
