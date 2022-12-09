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
        parent = None
        while node.left is not None:
            parent = node
            node = node.left
        min = node.value
        if parent is not None:
            parent.left = node.right
        
        return min
    
    def getMin(self):
        node = self
        parent = None
        while node.left is not None:
            parent = node
            node = node.left
        min = node.value
        return min

    def popMax(self):
        node = self
        parent = None
        while node.right is not None:
            parent = node
            node = node.right
        max = node.value
        if parent is not None:
            parent.right = node.left
        return max

    def remove(self, value, parent=None):
        node = self
        while node is not None:
            if value > node.value:
                parent = node
                node = node.right
            elif value < node.value:
                parent = node
                node = node.left
            else:
                if node.left is not None and node.right is not None:
                    node.value = node.right.getMin()
                    node.right.remove(node.value, node)
                # Root node case
                elif parent is None: 
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else: 
                        pass  # problem states to do nothing if you're deleting the root node, and the root node has no children
                elif node == parent.left:
                    parent.left = node.left if node.left is not None else node.right
                elif node == parent.right:
                    parent.right = node.left if node.left is not None else node.right
                break
        return self
        
    def myRemove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
    
        if value > self.value:
            if self.right is None:
                # value is not in tree, so do nothing
                return self
            self.right.remove(value, self)

        elif value < self.value:
            if self.left is None:
                # value is not in tree, so do nothing
                return self
            self.left.remove(value, self)
        else: # self.value == value

            if self.isLeaf():
                if parent is not None:  # value to remove is a leaf node, and not root
                    if self.value >= parent.value:
                        parent.right = None
                    else:
                        parent.left = None
                    return self
                else:
                    return self
            else:
                if self.right is not None:
                    self.value = self.right.popMin()
                else:
                    self.value = self.left.popMax()
        return self

def arrayToBST(array):
    bst = BST(array[0])
    for n in array[1:]:
        bst.insert(n)
    return bst

bst = arrayToBST([10, 5, 15, 2, 5, 13, 22, 1, 14])

def test(actual, expected):
    if expected == actual:
        print('Pass')
    else:
        print('Test failed')
        print('expected', expected)
        print('actual', actual)
    return expected == actual

def testPopMin():
    print("Testing popMin()")
    bst = arrayToBST([10, 5, 15, 2, 5, 13, 22, 1, 14])
    popped = bst.right.popMin()
    test(popped, 13)
    test(bst.right.left.value, 14)

def testPopMax():
    print("Testing popMax()")
    bst = arrayToBST([10, 5, 15, 2, 5, 13, 22, 1, 14])
    popped = bst.right.popMax()
    test(popped, 22)
    test(bst.right.right, None)

def testRemove():
    print("Testing remove()")
    bst = arrayToBST([10, 5, 15, 2, 5, 13, 22, 1, 14])
    bst.remove(10)
    test(bst.value, 13)
    test(bst.right.left.value, 14)

    bst.remove(1)
    test(bst.left.left.left, None)

    bst.remove(5)
    test(bst.left.value, 5)

    bst.remove(15)
    test(bst.right.value, 22)
    test(bst.right.left.value, 14)

    bst = arrayToBST([10, 5, 15, 2, 5, 13, 22, 1, 14])
    bst.remove(14)
    test(bst.right.left.isLeaf(), True)
    test(bst.right.left.value, 13)

    bst.remove(3)
    test(bst.left.left.value, 2)
    
    bst = BST(10)
    bst.remove(10)
    test(bst.value, 10)




testPopMin()
testPopMax()
testRemove()




