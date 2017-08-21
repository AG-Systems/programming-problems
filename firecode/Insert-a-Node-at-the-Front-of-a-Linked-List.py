class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    # Method for inserting a new node at the start of a Linked List   
    def insert_at_front(self,data):
        new = Node()
        new.setData(data)
        
        if not self.head:
            self.setHead(new)
        else:
            new.setNext(self.head)
            self.head = new
            
        
