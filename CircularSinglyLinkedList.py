class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node 
            if node.next==self.head:
                break
            node=node.next

    #Creation of circular singly linked list
    def createCSLL(self,value):
        node=Node(value)
        node.next=node
        self.head=node
        self.tail=node
        return "CSLL has been created"

    #Insertion in CSLL
    def insertCSLL(self,value,location=0):
        node=Node(value)
        #Check if LL is empty
        if self.head is None:
            self.head=node
            self.tail=node
            node.next=node
            return
        #Beginning
        if location==0:
            node.next=self.head
            self.head=node
            self.tail.next=node

        #End
        elif location==1:
            self.tail.next=node
            node.next=self.head
            self.tail=node

        #Middle
        else:
            index=0
            tmp_node=self.head
            while index<location-1:
                tmp_node=tmp_node.next
                index+=1
            node.next=tmp_node.next
            tmp_node.next=node

csll=CircularSinglyLinkedList()
#csll.createCSLL(1)
csll.insertCSLL(1,0)
csll.insertCSLL(1,0)
csll.insertCSLL(2,1)
csll.insertCSLL(3,1)
csll.insertCSLL(4,2)


print([node.value for node in csll])