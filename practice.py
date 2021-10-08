class Node:
    def __init__(self, value):
        self.value = value  # the value we pass when node is created
        self.next = None


def iterate_link(node):
    while node is not None:

        print(node.value)
        node = node.next


head = Node("1st node")
head.next = Node("second node")
#head.next.next = Node("third node")

iterate_link(head)
