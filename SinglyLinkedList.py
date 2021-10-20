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

    #Traversing linked list
    def traverseSLL(self):
        if self.head is None:
            print("No elements in linked list")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next


    #Searching for a value in LL
    def searchLL(self,value):
        if self.head is None:
            print("No elements in Linked List")
        else:
            node=self.head
            while node is not None:
                if node.value==value:
                    print("Element found")
                    return
                node=node.next
            print("Element not found")

    #Deleting a node
    def deleteNode(self,location):
        if self.head is None:
            print("No elements in LL")
            return 
        #Beginning
        if location==0:
            #Check if only one element
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
        #End
        elif location==1:
            #Check if only one element
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                node=self.head
                while node.next!=self.tail:
                    node=node.next
                self.tail=node
                node.next=None

        #Location given
        else:
            index=0
            node=self.head
            while index<location-1:
                node=node.next
                index+=1
            node.next=node.next.next

    #Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("No elements in SLL")
        else:
            self.head=None
            self.tail=None


sll=SLinkedList()
sll.insertSll(2)
sll.insertSll(1)
sll.insertSll(3,1)
sll.insertSll(5,1)
sll.insertSll(4,3)


print([node.value for node in sll])
#sll.traverseSLL()
sll.deleteNode(3)

sll.traverseSLL()