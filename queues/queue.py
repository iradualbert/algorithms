class Queue:
    def __init__(self):
        self.storage = {}
        self.head = 0
        self.count = 0
        
    def enqueue(self, element):
        self.storage[self.tail] = element
        self.tail +=1
        self.count += 1
        
    def dequeue(self):
        self.count -= 1
        removed = self.storage[self.head]
        del self.storage[self.head]
        self.head += 1
        return removed
    
    def is_empty(self):
        return self.count == 0
    
    def show(self):
        print(f"Head: {self.head}, Tail: {self.tail}, Count: {self.count}")
        if self.is_empty():
            print("The Queue is empty")
        else:
            for x in range(self.count):
                n = self.head + x
                print(f"#{n} - {self.storage[n]}")
        
