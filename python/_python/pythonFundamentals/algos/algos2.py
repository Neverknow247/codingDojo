class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, valueInput):
        # create a node (car) with that valueInput
        newNode = Node(valueInput)
        if self.head == None:  # if nobody is at front of line, then line is empty
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self

    def dequeue(self):
        if self.head != None:
            temp = self.head.value
            self.head = self.head.next
            return temp
        else:
            print("nothing in queue")
            return None

    def front(self):
        if self.head != None:
            return self.head.value
        else:
            print("nothing in queue")
            return None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def contains(self, valueToFind):
        runner = self.head
        while runner != None:
            if runner.value == valueToFind:
                return True
            runner = runner.next

        return False

    def size(self):
        runner = self.head
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        return count

    def display(self):
        runner = self.head
        output = ""
        while runner != None:
            output += f"{runner.value} -->"
            runner = runner.next
        print(output)
        return self


class Stack:
    def __init__(self):
        self.top = None

    def push(self, valueInput):
        newNode = Node(valueInput)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        return self

    def pop(self):
        temp = self.top.value
        self.top = self.top.next
        return temp

    def display(self):
        runner = self.top
        result = ""
        while runner != None:
            result += f"{runner.value}-->"
            runner = runner.next
        print(result)
        return self

    def contains(self, valueToFind):
        # HINT: to go from node to node, use a runner
        if self.top == None:
            print("no nodes in this list fam")
            return False
        else:
            runner = self.top
            while runner != None:
                if runner.value == valueToFind:
                    print("found the value!")
                    return True
                runner = runner.next
            return False

    def size(self):
        count = 0
        runner = self.top
        while runner != None:
            count += 1
            runner = runner.next
        return count



chikfilaDT = Queue()
chikfilaDT.enqueue(5).enqueue(8).enqueue(18).enqueue(15)

queue2 = Queue()
queue2.enqueue(5).enqueue(8).enqueue(8).enqueue(5)




# def isQueuePalindrome(queueInput):
#     stack1 = Stack()
#     tempStack = Stack()
#     stack2 = Stack()
#     while queueInput.head != None:
#         stack1.push(queueInput.front())
#         tempStack.push(queueInput.front())
#         queueInput.dequeue()
#     while tempStack.top != None:
#         stack2.push(tempStack.top.value)
#         tempStack.pop()
#     runner1 = stack1.top
#     runner2 = stack2.top
#     for i in range(stack1.size()):
#         if runner1 != None and runner2 != None:
#             if runner1.value == runner2.value:
#                 runner1 = runner1.next
#                 runner2 = runner2.next
#             else:
#                 print(False)
#                 return(False)
#     print(True)
#     return True

def isQueuePalindrome(queueInput):
    rStack = Stack()
    for i in range(queueInput.size()):
        temp = queueInput.dequeue()
        rStack.push(temp)
        queueInput.enqueue(temp)
    for i in range(queueInput.size()):
        if rStack.pop() != queueInput.dequeue():
            print(False)
            return False
    print(True)
    return True


isQueuePalindrome(chikfilaDT)
isQueuePalindrome(queue2)


# class Node:
#     def __init__(self, valueInput):
#         self.value = valueInput
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def enqueue(self, valueInput):
#         newNode = Node(valueInput)
#         if self.head == None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         return self

#     def dequeue(self):
#         if self.head != None:
#             self.head = self.head.next
#         return self

#     def front(self):
#         if self.head != None:
#             return self.head.value
#         return self

#     def contains(self, valueInput):
#         runner = self.head
#         while runner != None:
#             if runner.value == valueInput:
#                 return True
#             runner = runner.next
#         return False

#     def isEmpty(self):
#         if self.head == None:
#             return True
#         return False

#     def size(self):
#         counter = 0
#         if self.head != None:
#             runner = self.head
#             while runner != None:
#                 counter +=1
#                 runner = runner.next
#         return counter

#     def display(self):
#         runner = self.head
#         output = ""
#         while runner != None:
#             output += f"{runner.value} -->"
#             runner = runner.next
#         print(output)
#         return self

# chikfilaDT = Queue()
# chikfilaDT.enqueue("Brad").enqueue("Charles").enqueue("Dawn").display()
# chikfilaDT.dequeue().front()
# chikfilaDT.contains("Chares")
# chikfilaDT.isEmpty()
# chikfilaDT.size()


# class Node:
#     def __init__(self, valueInput):
#         self.value = valueInput
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, valueInput):
#         newNode = Node(valueInput)
#         if self.top == None:
#             self.top = newNode
#         else:
#             newNode.next = self.top
#             self.top = newNode
#         return self

#     def pop(self):
#         if self.top == None:
#             print('Nothing in stack')
#             return False
#         elif self.top != None:
#             self.top = self.top.next
#         return self

#     def display(self):
#         runner = self.top
#         result = ""
#         while runner != None:
#             result += f"{runner.value}-->"
#             runner = runner.next
#         print(result)
#         return self


# stak1 = Stack()
# stak1.push(5).push(12).push(24).push(10).display()
# stak1.pop().display()
