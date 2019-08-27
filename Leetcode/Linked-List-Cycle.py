# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        
        slow_pointer = head
        fast_pointer = head.next
        
        while slow_pointer != fast_pointer:
            if fast_pointer == None or fast_pointer.next == None:
                return False
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True
