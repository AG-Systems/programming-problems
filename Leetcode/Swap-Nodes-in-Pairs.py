# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        temp = head
        temp_next = head.next.next
        
        head = head.next
        head.next = temp
        head.next.next = temp_next

        head.next.next = self.swapPairs(head.next.next)
        return head
                
        
            
