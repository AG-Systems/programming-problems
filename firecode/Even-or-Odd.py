class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    def is_list_even(self):
        node = self.head
        counter = 0
        while node:
            node = node.getNext()
            counter += 1
        if counter % 2 == 0:
            return True
        else:
            return False
