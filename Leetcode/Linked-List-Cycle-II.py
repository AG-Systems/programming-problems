# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        hash_table = {}
        
        while head != None:
            if head in hash_table:
                return hash_table[head]
            else:
                hash_table[head] = head
            head = head.next    
