"""
LeetCode: 232. Implement Queue using Stacks

Problem: Implement a queue using two stacks

Solution: 
1. Before inserting some element. Push stack1 values to stack2 by popping. 
2. Then insert element to stack1. Then insert all elements from stack2 to stack1.

Time: Push is O(n)
Space: O(n)
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # self.stack1.insert(0, x)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()
        
    def peek(self) -> int:
        return self.stack1[-1]
        
    def empty(self) -> bool:
        return not self.stack1
