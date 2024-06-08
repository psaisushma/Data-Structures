class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Get size")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to push: ")
        stack.push(element)
        print("Element pushed:", element)
    elif choice == 2:
        popped_element = stack.pop()
        if popped_element is not None:
            print("Popped element:", popped_element)
        else:
            print("Stack is empty")
    elif choice == 3:
        peek_element = stack.peek()
        if peek_element is not None:
            print("Peek element:", peek_element)
        else:
            print("Stack is empty")
    elif choice == 4:
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == 5:
        print("Size of stack:", stack.size())
    elif choice == 6:
        break
    else:
        print("Invalid choice")
