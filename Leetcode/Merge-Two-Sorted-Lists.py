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
        if l1 == None or l2 == None:
            if l1:
                return l1
            else:
                return l2
            
        merge_list_head = None
        if l1.val > l2.val:
            merge_list_head = ListNode(l2.val)
            l2 = l2.next
        else:
            merge_list_head = ListNode(l1.val)
            l1 = l1.next
            
        head = merge_list_head
        while l1 and l2:
            new_node = None
            if l1.val > l2.val:
                new_node = ListNode(l2.val)
                l2 = l2.next
            else:
                new_node = ListNode(l1.val)
                l1 = l1.next
            merge_list_head.next = new_node
            merge_list_head = merge_list_head.next
        if l1:
            merge_list_head.next = l1
        if l2:
            merge_list_head.next = l2
        return head
        
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
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
            
  """      
