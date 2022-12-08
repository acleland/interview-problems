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
            return True
        if value >= self.value:
            if self.right is None:
                return False
            return self.right.contains(value)
        if self.left is None:
            return False
        return self.left.contains(value)


    def isLeaf(self):
        return (self.left is None) and (self.right is None)

    def popMin(self):
        node = self
        while node.left is not None:
            parent = node
            node = node.left
        min = node.value
        if node.right is not None:
            parent.left = node.right
        else:
            parent.left = None
        return min

        
    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        if value > self.value:
            if self.right is None:
                # value is not in tree, so do nothing
                return self
            self.right.remove(value)

        elif value < self.value:
            if self.left is None:
                # value is not in tree, so do nothing
                return self
            self.left.remove(value)
        else: # self.value == value
            pass
        return self
