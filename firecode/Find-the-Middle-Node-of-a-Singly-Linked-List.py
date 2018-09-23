class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    def find_middle_node(self):
        fast = self.head.next
        slow = self.head
        
        while fast:
            if fast.next:
                fast = fast.next
            else:
                return slow
            fast = fast.next
            slow = slow.next
        return slow
