"""
Validate BST

Write a function that takes in a potentially invalid Binary Search Tree and returns
a boolean representing whether the BST is valid.


"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min=float('-inf'), max=float('inf')):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    return validateBst(tree.left, min, tree.value) and validateBst(tree.right, tree.value, max)
    