class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Node:
    def __init__(self,value):
        self.value =value
        self.next=None

sll=SLinkedList()
node1=Node(1)
node2=Node(2)
sll.head=node1
node1.next=node2
sll.tail=node2
#print(sll.head.value)