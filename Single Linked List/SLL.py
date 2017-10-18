__author__ = 'Abhishek'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print("....END....")

    def insertatbeg(self, x):
        new_node = Node(x)

        new_node.next = self.head

        self.head = new_node

    def insertafter(self, prev_node, x):
        tag, node = LinkedList.findnode(self, prev_node)
        if tag is True:
            new_node = Node(x)

            new_node.next = node.next

            node.next = new_node
        else:
            print("Previous element not found.....")

    def findnode(self, x):
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data is x:
                    return True, temp
                temp = temp.next
            return None


if __name__ == '__main__':

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printlist()

    llist.insertatbeg(4)
    llist.printlist()

    llist.insertafter(4, 2)
    llist.printlist()

