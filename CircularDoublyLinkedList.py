class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    def createCDLL(self,value):
        node=Node(value)
        node.prev=node
        node.next=node
        self.head=node
        self.tail=node

    def insertCDLL(self,value,location):
        if self.head is None:
            print("CDLL does not exist")
            return
        node=Node(value)
        #Begin
        if location==0:
            node.next=self.head
            node.prev=self.tail
            self.tail.next=node
            self.head.prev=node
            self.head=node
        #End
        elif location==1:
            node.prev=self.tail
            node.next=self.head
            self.tail.next=node
            self.head.prev=node
            self.tail=node
        #Between
        else:
            index=0
            tmpNode=self.head
            while index<location-1:
                tmpNode=tmpNode.next
                index+=1
            node.next=tmpNode.next
            node.prev=tmpNode
            tmpNode.next.prev=node
            tmpNode.next=node

    def traverseCDLL(self):
        if self.head is None:
            print("CDLL is empty!")
            return
        node=self.head
        while node:
            print(node.value)
            if node.next==self.head:
                break
            node=node.next

    def reverseTraverseCDLL(self):
        if self.head is None:
            print("CDLL is empty!")
            return
        node=self.tail
        while node:
            print(node.value)
            if node==self.head:
                break
            node=node.prev

    def searchCDLL(self,value):
        if self.head is None:
            print("CDLL is empty!")
            return
        node=self.head  
        while node:
            if node.value==value:
                print("Element found")
                return
            if node==self.tail:
                break
            node=node.next
        print("Element not found")

    def deleteNode(self,location):
        if self.head is None:
            print("CDLL is empty!")
            return          
        #Begin
        if location==0:
            if self.head==self.tail:
                self.head.prev=None
                self.head.next=None
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.tail.next=self.head                
                self.head.prev=self.tail
        #End
        elif location==1:
            if self.head==self.tail:
                self.head.prev=None
                self.head.next=None
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.head.prev=self.tail
                self.tail.next=self.head
        #Between
        else:
            index=0
            tmpNode=self.head
            while index<location-1:
                tmpNode=tmpNode.next
                index+=1
            tmpNode.next=tmpNode.next.next
            tmpNode.next.prev=tmpNode
            
    def deleteCDLL(self):
        if self.head is None:
            print("CDLL is empty!")
            return
        node=self.head
        self.tail.next=None
        while node:
            node.prev=None
            node=node.next
        self.head=None
        self.tail=None
        print("CDLL has been successfully deleted")





cdll=CircularDoublyLinkedList()
cdll.createCDLL(1)
cdll.insertCDLL(2,0)
cdll.insertCDLL(1,0)
cdll.insertCDLL(3,1)
cdll.insertCDLL(4,1)
cdll.insertCDLL(5,2)
print([node.value for node in cdll])
cdll.deleteNode(3)
#cdll.deleteCDLL()
print([node.value for node in cdll])