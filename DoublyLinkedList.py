
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def createDLL(self,value):
        node=Node(value)
        self.head=node
        self.tail=node

    def insertDLL(self,value,location):
        if self.head is None:
            print("DLL does not exist.")
            return
        node=Node(value)
        #Begin
        if location==0:
            node.next=self.head
            node.prev=None
            self.head.prev=node
            self.head=node
        #End
        elif location==1:
            self.tail.next=node
            node.prev=self.tail
            node.next=None
            self.tail=node
        #Middle
        else:
            tmpNode=self.head
            index=0
            while index<location-1:
                tmpNode=tmpNode.next
                index+=1
            node.next=tmpNode.next
            node.prev=tmpNode
            tmpNode.next.prev=node
            tmpNode.next=node

    def traverseDLL(self):
        if self.head is None:
            print("DLL is empty!")
            return
        node=self.head
        while node:
            print(node.value)
            node=node.next
    
    def reverseTraverseDLL(self):
        if self.head is None:
            print("DLL is empty!")
            return
        node=self.tail
        while node:
            print(node.value)
            node=node.prev

    def searchDLL(self,value):
        if self.head is None:
            print("DLL is empty")
            return
        node=self.head
        while node:
            if node.value==value:
                print("Element found")
                return
            node=node.next
        print("Element not found")

    def deleteNode(self,location):
        if self.head is None:
            print("DLL is empty")
            return
        #Begin
        if location==0:
            #One element
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=None
                
        #End
        elif location==1:
            #One element
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None
                

        #Middle
        else:
            node=self.head
            index=0
            while index<location-1:
                node=node.next
                index+=1
            newNode=node.next
            node.next=newNode.next
            newNode.next.prev=node
        print("The node has been successfully deleted")

    def deleteDLL(self):
        if self.head is None:
            print("DLL is empty")
            return
        node=self.head
        while node:
            node.prev=None
            node=node.next
        self.head=None
        self.tail=None
        print("The DLL has been successfully deleted")
    

dll=DoublyLinkedList()
dll.createDLL(1)
dll.insertDLL(2,0)
dll.insertDLL(3,0)
dll.insertDLL(4,1)
dll.insertDLL(5,2)

print([node.value for node in dll])
#dll.reverseTraverseDLL()
dll.searchDLL(3)
dll.deleteNode(2)
#dll.deleteDLL()
print([node.value for node in dll])
