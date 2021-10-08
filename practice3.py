class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):

        self.head = None

    def append(self, value):

        if self.head is None:

            new_node = Node(value)

            new_node.prev = None
            self.head = new_node
            print("head Node ceated:", self.head.value)
            return

        else:
            new_node = Node(value)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                new_node.prev = current_node

                new_node.next = None
                print("Appended new Node with value", self.tail.value)


llist = DoublyLinkedList()
llist.append("this might not be working")
llist.append("I hope this works")
