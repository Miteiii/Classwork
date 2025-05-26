class LinkedlistNode:
    def __init__(self, value, nextNode = None):
        #   init initialises variables
        self.value = value
        self.nextNode = nextNode

node1 = LinkedlistNode("1")
node2 = LinkedlistNode("2")
node3 = LinkedlistNode("3")
node4 = LinkedlistNode("4")
node5 = LinkedlistNode("5")
node6 = LinkedlistNode("6")
node7 = LinkedlistNode("7")
node8 = LinkedlistNode("8")
node9 = LinkedlistNode("9")
node10 = LinkedlistNode("10")



node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
node8.nextNode = node9
node9.nextNode = node10

currentNode = node1
while True:
    print(currentNode.value, ">>>", end = ' ')

    if currentNode.nextNode is None:  #Check if the current Node is the last Node
        print("None")
        break
    currentNode = currentNode.nextNode
            #EXPLANATION OF WHAT IS HAPPENING.(Python way of doing it)
    #It starts at the head of the linked list (node1).
    # Prints the value of the current node.
    # Checks if nextNode is None (i.e., it's the last node).
    # If not, it moves to the next node.
    # Stops when the end of the list is reached.