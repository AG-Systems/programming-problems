class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self,data):
        new = Node()
        new.setData(data)
        if self.head == None:
            self.head = new
        else:
            current  = self.head
            while current.getNext() != None:
                current = current.next
            current.setNext(new)
