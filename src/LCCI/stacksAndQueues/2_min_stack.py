'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? 
Push, pop and min should all operate in O(1) time.
'''

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        current_min = min(value, self.stack[-1] if self.stack else value)
        self.min_stack.append(current_min)

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()