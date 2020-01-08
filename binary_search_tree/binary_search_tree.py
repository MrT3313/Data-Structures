import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #  LEFT - if <
        if value < self.value:
            # EMPTY - make new node w/ own val, left, right
            if not self.left:
                self.left = BinarySearchTree(value)
            #  NOT empty - call insert again on that left node instead 
            else: 
                self.left.insert(value)

        #  RIGHT - if > 
        else: 
            if not self.right:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # goal
        if target == self.value: 
            return True

        # Check Left
        if target < self.value:
            # no left child node
            if not self.left:
                return False
            #  continue - call contains again on left child node
            else:
                return self.left.contains(target)
        # Check Right
        else:
            if not self.right: 
                return False
            else: 
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value

        while self:
            if self.value > max: 
                max = self.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if not self: 
            return
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        
        # Iterate
        cb(self.value)







    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
