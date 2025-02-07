### **Simply Linked List**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            del self.head
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        del temp.next
        temp.next = None

    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            del temp
            return
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        del temp

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
ll.insert_at_position(2, 1.5)
ll.display()

ll.delete_from_beginning()
ll.display()

ll.delete_from_end()
ll.display()

ll.delete_node(2)
ll.display()

print("Search 3:", ll.search(3))
print("Search 5:", ll.search(5))

```

### **Circular Linked List**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp.next == self.head:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if self.head.next == self.head:
            self.head = None
            del temp
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        last.next = self.head
        del temp

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if self.head.next == self.head:
            self.head = None
            del temp
            return
        while temp.next.next != self.head:
            temp = temp.next
        del temp.next
        temp.next = self.head

    def delete_node(self, key):
        if self.head is None:
            return
        temp = self.head
        prev = None
        while temp.data != key:
            if temp.next == self.head:
                return
            prev = temp
            temp = temp.next
        if temp == self.head and temp.next == self.head:
            self.head = None
        elif temp == self.head:
            prev = self.head
            while prev.next != self.head:
                prev = prev.next
            self.head = temp.next
            prev.next = self.head
        else:
            prev.next = temp.next
        del temp

    def search(self, key):
        if self.head is None:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

# Example usage
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_beginning(0)
cll.insert_at_position(2, 1.5)
cll.display()

cll.delete_from_beginning()
cll.display()

cll.delete_from_end()
cll.display()

cll.delete_node(2)
cll.display()

print("Search 3:", cll.search(3))
print("Search 5:", cll.search(5))
```

### **Doubly Linked List**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del temp

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            del temp
            return
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
        del temp

    def delete_node(self, key):
        temp = self.head
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None:
            return
        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        del temp

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_beginning(0)
dll.insert_at_position(2, 1.5)
dll.display()

dll.delete_from_beginning()
dll.display()

dll.delete_from_end()
dll.display()

dll.delete_node(2)
dll.display()

print("Search 3:", dll.search(3))
print("Search 5:", dll.search(5))
```