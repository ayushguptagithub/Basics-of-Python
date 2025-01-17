## **Stack**
```python
class Stack:
    def __init__(self):
        self.size = int(input("Enter the size:"))
        self.top=-1
        self.stack = [0 for x in range(self.size)]

    def push(self, item):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.stack[self.top] = item
            self.display()

    def pop(self):
        if  self.is_empty():
            print("Stact is Empty")
        else:
            self.top -= 1
            self.stack.pop()
            self.display()

    def peek(self):
        if not self.is_empty():
            print(self.stack[-1])
        else:    
            print("Peek from an empty stack")

    def is_empty(self):
        if self.top==-1:
            return True
        return False
        
    def isFull(self):
        if self.top == self.size-1:
            return True
        return False
        
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])

   

# Usage Example:
stack = Stack()
while True:
    ch = int(input("Enter 1:Push\n2:Pop\n3:peek\nEnter:"))
    if ch==1:
        n = int(input("Enter the item:"))
        stack.push(n)
    elif ch==2:
        
        stack.pop()
    elif ch==3:
        stack.peek()
    elif ch==4:
        print("Exiting")
        break
    else:
        print("Invalid")
        
        
```


