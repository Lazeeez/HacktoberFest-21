# Python program to find the middle of a given linked list


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # create Node and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        temp = self.head
        count = 0

        while self.head:

            # only update when count is odd
            if count & 1:
                temp = temp.next
            self.head = self.head.next

            # increment count in each iteration
            count += 1

        print(temp.data)


# Driver code
llist = LinkedList()
llist.push(1)
llist.push(20)
llist.push(100)
llist.push(15)
llist.push(35)
llist.printMiddle()
