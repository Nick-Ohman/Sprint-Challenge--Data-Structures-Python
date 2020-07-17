from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            self = BSTNode(value)
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


        


    # Return the maximum value found in the tree
    def get_max(self):
        ## how do i keep going right to get 15?
        # res = self
        # rres = get_max(root.right)
        # if (rres > res):  
        #     res = rres  
        # return res
        if self.right:
            return self.right.get_max()
        else:
            return self.value

       

        



        # find the max value in the tree
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
       ## we need to hit ever node
        fn(self.value)
        #left
        if self.left:
           self.left.for_each(fn)
        #right
        if self.right:
            self.right.for_each(fn)
        # 

        # What Matt instructor did
        # why is this the first line??
        #fn(self.value)
        #if self.right is not None:
            #self.right.for_each(fn)
        #if self.left is not None:
            #self.left.for_each(fn)

        ### seans iterate solution
        #DFT:LIFO - use a stack
       


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        # lowest number is always to the left

        #recursion means

        #base case
        # if node is passed in is none
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

        #build up your call stack to see what happens

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        #use queue
        # start queue with root node
        queue.append(self)
        #while loop that checks size of queue
            # pointer variable that updates on start of loop
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        #use a stack
        #start stack with root node
        stack.append(self)
        #while loop that checks stack size
            #use pointer
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.right)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

