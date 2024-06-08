class Queue:
    def __init__(self):
        self.queue = []
        self.size = 5
        self.rear = self.front = -1

    def enqueue(self, data):
        if self.rear < self.size - 1:
            self.queue.append(data)
            if self.front == -1:
                self.front = 0
            self.rear += 1
        else:
            print("Queue is full")

    def dequeue(self):
        if self.rear == -1 or self.rear < self.front:
            print("Queue is empty")
        else:
            self.queue.pop(self.front)
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1

    def display(self):
        if self.rear == -1 or self.rear < self.front:
            print("Queue is empty")
        else:
            for elem in self.queue[self.front:self.rear + 1]:
                print(elem)

def main():
    q = Queue()

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data to enqueue: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()