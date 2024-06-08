class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def delete(self):
        if self.head is None:
            print("The list is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    def delete_last(self):
        if self.head is None:
            print("The list is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    def delete_by_element(self, element):
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current:
                if current.data == element:
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.head = current.next
                    if current.next:
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev
                    return
                current = current.next
            print("Element not found")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
obj = DoubleLinkedList()
while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete from beginning")
    print("4. Delete from end")
    print("5. Delete by element")
    print("6. Display")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data to insert at beginning: "))
        obj.insert_begin(data)
    elif choice == 2:
        data = int(input("Enter the data to insert at end: "))
        obj.insert_end(data)
    elif choice == 3:
        obj.delete()
    elif choice == 4:
        obj.delete_last()
    elif choice == 5:
        element = int(input("Enter the element to delete: "))
        obj.delete_by_element(element)
    elif choice == 6:
        obj.display()
    elif choice == 7:
        break
    else:
        print("Invalid choice")