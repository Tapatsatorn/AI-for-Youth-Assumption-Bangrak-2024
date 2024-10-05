#linked list
#example
try:
    class Node:
        def __init__(self,next=None, previous=None, head=None, tail=None):
            self.head = head
            self.tail = tail
            self.next = next
            self.previous = previous

    if __name__ == '__main__':
        node1 = Node()
        node2 = Node()
        node3 = Node()

        node1.next = node2
        node1.head = node1
        node2.next = node3
        node3.tail = node3

        print(node1.next)
        print(node1.head)
        print(node2.next)
        print(node3.tail)
except:
    ...
