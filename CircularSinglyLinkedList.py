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


    def traverseCSLL(self):
        if self.head is None:
            print("CSLL is empty")
        else:
            node=self.head
            while True:
                print(node.value)
                if node.next==self.head:
                    break
                node=node.next


    def searchCSLL(self,value):
        if self.head is None:
            print("CSLL is empty")
            return
        node=self.head
        while node:
            if node.value==value:
                print("Element found")
                return
            if node.next==self.head:
                print("Element not found")
                return
            node=node.next

    def deleteNode(self,location):
        if self.head is None:
            print("CSLL is empty")
            return
        #Begin
        if location==0:
            if self.head==self.head.next:
                self.tail.next=None
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.tail.next=self.head
        #End
        elif location==1:
            if self.head==self.head.next:
                self.tail.next=None
                self.head=None
                self.tail=None
            else:
                node=self.head
                while node.next!=self.tail:
                    node=node.next
                node.next=self.head
                self.tail=node
        #Middle
        else:
            index=0
            node=self.head
            while index<location-1:
                node=node.next
                index+=1
            newNode=node.next
            node.next=newNode.next


    def deleteEntireCSLL(self):
        if self.head is None:
            print("CSLL is already empty")
            return
        self.tail.next=None
        self.head=None
        self.tail=None




csll=CircularSinglyLinkedList()
#csll.createCSLL(1)
csll.insertCSLL(1,0)
csll.insertCSLL(1,0)
csll.insertCSLL(2,1)
csll.insertCSLL(3,1)
csll.insertCSLL(4,2)


print([node.value for node in csll])
#csll.traverseCSLL()
csll.searchCSLL(3)
csll.deleteNode(3)
#csll.deleteEntireCSLL()
print([node.value for node in csll])