# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        tail_p1 = None
        tail_p2 = None
        while p1 != p2:
            if p1:
                p1 = p1.next
                if p1 and p1.next == None:
                    tail_p1 = p1
            else:
                p1 = headB
            
            if p2:
                p2 = p2.next
                if p2 and p2.next == None:
                    tail_p2 = p2
            else:
                p2 = headA
            
            if tail_p1 and tail_p2:
                if tail_p1 != tail_p2:
                    return None
        return p1
