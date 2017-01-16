# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        tail = head
        r = None
        while node:
            while tail:
                if tail.next != None:
                    tail = tail.next
            node = tail.val
            node = node.next
        return head
            
            
