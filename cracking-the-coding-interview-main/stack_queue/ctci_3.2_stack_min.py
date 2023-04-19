"""
LeetCode: 155. Min Stack

Problem: Design a stack that supports push, pop, min which retrieves the minimum element in constant time.

Solution: 
1. Save min element for each element;

Time: All operations are O(1)
Space: O(n)
"""


class MinStack:
    def __init__(self):
        self.A = []  # Stack
        self.M = []  # Min number for each element of stack
        
    def push(self, x):
        self.A.append(x)
        
        if not self.M:
            self.M.append(x)
        else:
            self.M.append(min(x, self.M[-1]))
            
        print(self.A, self.M)
        
    def pop(self):
        self.A.pop()
        self.M.pop()
        
    def top(self):
        return self.A[-1]
    
    def getMin(self):
        return self.M[-1]
