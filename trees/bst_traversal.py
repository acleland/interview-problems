"""
BST Traversal

Write three functions that take in a Binary Search Tree and an empty array,
traverse the BST, add its nodes' values to the input array, and return that
array. The three functions should traverse the BST using in-order, pre-order,
and post-order tree-traversal techniques.

"""

def inOrderTraverse(tree, array):
    if tree is None:
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is None:
        return array
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is None:
        return array
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array