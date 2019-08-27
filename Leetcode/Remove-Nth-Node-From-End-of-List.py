# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        seeker = dummy
        current = dummy
        
        x = 1
        while x <= n + 1:
            seeker = seeker.next
            x += 1
            
        while seeker:
            current = current.next
            seeker = seeker.next
        
        current.next = current.next.next
        return dummy.next
            
