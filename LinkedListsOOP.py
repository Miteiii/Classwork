class Node:
    def __init__(self, data):  #we pass data
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):  #we dont pass anything here. why? we're just initializing an empty linked list.
        self.head = None

    def insertAtTheBeggining(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')

#Haven't called or defined these methods yet thus no output
            temp = temp.next
        print()

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None: # (means the list is empty)
           new_node = new_node #Making it the last node
           return None

        last = self.head

        while last.next:
            last = last.next #Making the last.next to be the new one which is gonna none
        last.next = new_node

#we haven't imported so it won't run it.
if __name__ == '__main__': #Only run the following block of code if this
# file is being run directly — not imported as a module
    llist = Linkedlist()

    #((Quick brown fox), it'll insert them at the beggining, thus writing it in ana inverted manner
    llist.insertAtTheBeggining("Fox")
    llist.insertAtTheBeggining("Brown")
    llist.insertAtTheBeggining("Quick")
    llist.insertAtTheBeggining("The")

    llist.printLinkedlist()

    llist.insertAtTheEnd("Jumps")
    llist.insertAtTheEnd("Over")
    llist.insertAtTheEnd("The")
    llist.insertAtTheEnd("Fence")

    llist.printLinkedlist()