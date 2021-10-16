class Node:
    #Initialize node oject
    def __init__(self, data):
        self.data = data    #assign data
        self.next = None    #declare next as null

class LinkedList:
    #Initialize head
    def __init__(self):
        self.head = None

    #### Insert in the beginning
    def push(self, content):
        #Allocate node, Put data
        new_node = Node(content)
        #attach head after new_node
        new_node.next = self.head
        #set new_node as current head
        self.head = new_node

    #### Insert in the middle
    def insertAfter(self, prev_node, content):
        if prev_node is None:
            print("Prev Node invalid")
            return
        
        new_node = Node(content)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #### Insert at last
    def append(self, content):

        new_node = Node(content)
        #If Linkedlist is empty
        if self.head is None:
            self.head = new_node
            return
        #Else, traverse to last node
        last = self.head
        while (last.next):
            last = last.next
        #attach new node
        last.next = new_node

    ### PRINT LIST
    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    #### Delete node using key
    def deleteNode_key(self, key):
        temp = self.head
        #for head node
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        #moving ahead from head node, until key found
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        #if not found
        if temp == None:
            return
        #Unlink node
        prev.next = temp.next
        temp = None

    #### Delete node using position
    def deleteNode_pos(self, pos):
        if self.head is None:
            return
        
        temp = self.head
        #to delete head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        #find previous node of the node to be deleted
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        #store next to next node to be deleted
        next = temp.next.next
        #unlink 
        temp.next = None
        temp.next = next

    #### Find length
    def listlength(self):
        len = 0
        if self.head is None:
            print("Len = ",len)
            return

        temp = self.head
        while temp:
            len += 1
            temp = temp.next
        print("Len = ", len)

    #### REVERSE
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(6)
    list1.append(3)
    list1.push(4)
    list1.insertAfter(list1.head.next, 1)
    
    list1.printlist()
    print("______")

    list1.listlength()
    print("______")

    list1.deleteNode_key(4)
    list1.printlist()
    print("______")

    list1.reverse()
    list1.printlist()
    print("______")

    list1.deleteNode_pos(1)
    list1.printlist()
    print("______")


