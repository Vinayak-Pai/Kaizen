class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):

        node = self.head

        if node.data == Removekey:
            self.head = node.next
            node = None
            return
        prev = node
        nd = node.next

        while(nd.data !=Removekey):
            prev = nd
            nd = nd.next

        prev.next = nd.next
        nd = None


    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next




llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()