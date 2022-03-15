class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    # adds a node to the top of the stack
    def push(self,item):
        if self.length == 0:
            self.top = Node(item)
            self.bottom = Node(item)
        else:
            newNode = Node(item)
            newNode.next = self.top
            self.top = newNode
            return self.top
        self.length+=1

    # removes a node from the top of the stack
    def pop(self):
        self.top = self.top.next
        self.length-=1
        return self.top

    def peek(self):
        return self.top

    def display(self):
        elem = []
        currNode = self.top
        while currNode != None:
            elem.append(currNode.value)
            currNode = currNode.next
        return elem