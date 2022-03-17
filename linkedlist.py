class Node:
    
    def __init__(self,value=None):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display(self):
        elems = []
        currNode = self.head
        while currNode != None:
            elems.append(currNode.value)
            currNode = currNode.next
        return elems
    
    def append(self,value):
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = self.tail.next
        self.length+=1
        return self.head

    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length+=1
        return self.head

    def traverseToIndex(self,index):
        # If list = [10 --> 20 --> 30 --> 40 --> null], traverseToIndex(2) => [10-->20-->30-->null]
        currIndex = 0
        currNode = self.head
        while currIndex != index:
            currNode = currNode.next
            currIndex+=1
        return currNode
    
    def insert(self,index,value):
        newNode = Node(value)
        leader = self.traverseToIndex(index-1)
        holdingPointer = self.traverseToIndex(index)
        leader.next = newNode
        newNode.next = holdingPointer
        return leader

    def remove(self,index):
        if index > self.length-1:
            print("Index Out of range")
        else:
            leader = self.traverseToIndex(index-1)
            holdingPointer = self.traverseToIndex(index+1)
            leader.next = holdingPointer
            self.length-=1
            return leader
    
    def pop(self):
        leader = self.traverseToIndex(self.length-2)
        leader.next = None

    def reverse(self):
        currNode = self.head
        self.head = Node(currNode.value)
        while currNode.next != None:
            currNode = currNode.next
            self.prepend(currNode.value)
        
        # Updating the tail so that values can be added to the lists
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
            self.tail = currNode

        return self.head
