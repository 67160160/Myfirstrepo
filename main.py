class Stack:
    def __init__(self):
        self.ans = []
        
    def push(self, x):
        self.ans.append(x)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty!" 
        return self.ans.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.ans[-1]
    
    def is_empty(self):
        return len(self.ans) == 0

    def size(self):
        return len(self.ans)


s = Stack()

print(f"Is empty? {s.is_empty()}")

for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())

print("Pop from empty:", s.pop())
