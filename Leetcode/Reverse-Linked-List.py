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
        r = head
        container = []
        while node:
            container.append(node.val)
            node = node.next
        container = container[::-1]
        counter = 0
        while r:
            r.val = container[counter]
            r = r.next
            counter += 1
        return head
            
"""
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        def helper(current, prev = None):
            if current == None:
                return prev
            
            future = current.next
            current.next = prev
            prev = current
            current = future
            return helper(current, prev)
        
        return helper(head)
"""
