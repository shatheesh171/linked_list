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


dll=DoublyLinkedList()
dll.createDLL(1)

print([node.value for node in dll])