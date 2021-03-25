# STACK DATA STRUCTURE

# PUSH
# POP
# PEEK
# SIZE 

class Stack:
    def __init__(self):
        self.storage = {}
        self.count = 0
        
    def push(self, element):
        self.storage[self.count] = element
        self.count +=1
        
    def pop(self):
        if self.count == 0:
            return None
        removed = self.storage[self.count - 1]
        del self.storage[self.count - 1]
        self.count -=1
        return removed
    
    def peek(self):
        if self.count == 0:
            return None
        return self.storage[self.count - 1]
    
    
    def size(self):
        return self.count