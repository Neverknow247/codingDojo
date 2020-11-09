class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, valueInput):
        newNode = Node(valueInput)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self

    def dequeue(self):
        if self.head != None:
            self.head = self.head.next
        return self
    
    def front(self):
        if self.head != None:
            return self.head.value
        return self

    def contains(self, valueInput):
        runner = self.head
        while runner != None:
            if runner.value == valueInput:
                return True
            runner = runner.next
        return False

    def display(self):
        runner = self.head
        output = ""
        while runner != None:
            output += f"{runner.value} -->"
            runner = runner.next
        print(output)
        return self

chikfilaDT = Queue()
chikfilaDT.enqueue("Brad").enqueue("Charles").enqueue("Dawn").display()
chikfilaDT.dequeue().front()
chikfilaDT.contains("Chares")

