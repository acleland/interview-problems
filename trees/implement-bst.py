# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return true
        if value >= self.value:
            if self.right is None:
                return False
            return self.right.contains(value)
        if self.left is None:
            return False
        return self.left.contains(value)


    def isLeaf(self):
        return (self.left is None) and (self.right is None)
        
    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.isLeaf():
            return self
        elif (value == self.left.value) and self.left.isLeaf()
        return self
