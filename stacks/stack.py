# METHODS
# PUSH
# PEEK
# POP
# SIZE
# IS_EMPTY

class Stack:
    def __init__(self):
        self.storage = {}
        self.count = 0
        
    def pop(self):
        if self.count == 0:
            return None
        removed = self.storage[self.count - 1]
        del self.storage[self.count - 1]
        self.count -= 1
        return removed

    def push(self, element):
        self.storage[self.count] = element
        self.count += 1

    def peek(self):
        if self.count == 0:
            return None
        return self.storage[self.count - 1]

    def size(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
        
    # let's add one more methods for printing the stack elements
    def show(self):
        # I wanna get the values of the storage
        values = self.storage.values()
        # then I wanna print them a list
        print(list(values))
# stack = Stack()
# stack.push(100)
# stack.peek()
# stack.push(200)



# def is_palindrome(word):
#     stack = Stack()
#     for char in word:
#         stack.push(char)
#     reversed_word = stack.pop()
#     while not stack.is_empty():
#         reversed_word += stack.pop()
#     if reversed_word == word:
#         print(f"{word} is a palindrome")
#     else:
#         print(f"{word} is not a palindrome")


# if __name__ == "__main__":
#     is_palindrome("racecar")
#     is_palindrome("madam")
#     is_palindrome("money")

