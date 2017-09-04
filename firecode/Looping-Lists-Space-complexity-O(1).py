class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def is_cyclic(self):
        og_head = self.head
        node = self.head
        while node:
            node = node.getNext()
            if node == og_head:
                return True
        return False
