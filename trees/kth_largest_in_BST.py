"""
Find the Kth Largest Value in BST

Write a function that takes a Binary Search Tree and an integer, k as parameters
and returns the kth largest integer in the BST. 

"""
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, visited, lastValue):
        self.visited = visited
        self.lastValue = lastValue
        

def findKthLargestValueInBst(tree, k):
    # Perform a reverse in-order traversal
    # visit right, visit self, visit left

    treeInfo = TreeInfo(0, -1)
    reverseInOrder(tree, k, treeInfo)
    return treeInfo.lastValue
    
    
def reverseInOrder(tree, k, treeInfo):
    if tree is None or treeInfo.visited >= k:
        return
    reverseInOrder(tree.right, k, treeInfo)
    if treeInfo.visited < k:
        treeInfo.visited += 1
        treeInfo.lastValue = tree.value
    reverseInOrder(tree.left, k, treeInfo)