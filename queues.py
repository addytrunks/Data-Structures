class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length=0
    
    # adds an item to the end , similar to append
    def enqueue(self,item):
        newNode = Node(item)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length+=1
        return self.first
    
    # removes an item from the top
    def dequeue(self):
        self.first = self.first.next
        self.length-=1
        return self.first

    def display(self):
        elem=[]
        currNode = self.first
        while currNode!=None:
            elem.append(currNode.value)
            currNode = currNode.next
        return elem