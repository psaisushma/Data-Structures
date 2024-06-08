class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.head = self.head.next
    def delete_last(self):
        if self.head is None:
            print("The list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
    def delete_by_element(self, element):
        if self.head is None:
            print("The list is empty")
        else:
            if self.head.data == element:
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.data == element:
                    current.next = current.next.next
                    return
                current = current.next
            print("Element not found")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
obj = LinkedList()
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