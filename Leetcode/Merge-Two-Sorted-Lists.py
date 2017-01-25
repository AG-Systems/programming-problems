# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        container = []
        while n1:
            container.append(n1.val)
            n1 = n1.next
        while n2:
            container.append(n2.val)
            n2 = n2.next
        container.sort()
        return container
            
        
