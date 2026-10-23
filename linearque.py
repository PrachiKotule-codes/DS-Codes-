# Circular Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

        print(value, "inserted into queue")

    def dequeue(self):
        if self.front is not None:
            temp = self.front

            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.rear.next = self.front

            print(temp.data, "deleted from queue")
        else:
            print("Queue is empty")

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front

            while True:
                print(temp.data, end=" -> ")
                temp = temp.next

                if temp == self.front:
                    break

            print("(back to front)")


# Main program
q = CQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()