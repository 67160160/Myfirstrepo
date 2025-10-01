class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    #test

if __name__=="__main__":
    stack = Stack()

    print("Stack ว่างหรือไม่:", stack.size())
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("ขนาดของ Stack:", stack.size())
    print("ข้อมูลบนสุด:", stack.peek())

    print("นำข้อมูลออก:", stack.pop())
    print("นำข้อมูลออก:", stack.pop())

    print("ขนาดของ Stack หลังจาก pop:", stack.size())
    print("Stack ว่างหรือไม่:", stack.is_empty())