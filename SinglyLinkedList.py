class Node:
    def __init__(self,value=None):
        self.value =value
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insertSll(self,value,location=0):
        newNode=Node(value)
        #Check if any element exist
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            return
        #Beginning
        if location==0:
            newNode.next=self.head
            self.head=newNode
        #End
        elif location==1:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode
        #Middle
        else:
            tempNode=self.head
            index=0
            while index<location-1:
                tempNode=tempNode.next
                index+=1

            newNode.next=tempNode.next
            tempNode.next=newNode


sll=SLinkedList()
sll.insertSll(2)
sll.insertSll(1)
sll.insertSll(3,1)
sll.insertSll(5,1)
sll.insertSll(4,3)


print([node.value for node in sll])