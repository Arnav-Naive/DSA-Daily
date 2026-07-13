# List implimentation of Queue  

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]

        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
        
    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]

    def size(self):
        return len(self.q) - self.front
        
    
"""not the best way to implement queue"""
"""The reason is that list in Python is dynamic array based, 
and every time you remove an element from the front, 
all the other elements shift one position to the left,
 which takes O(n) time in the worst case"""