# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
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
        container.sort()
        counter = 0
        while r:
            r.val = container[counter]
            r = r.next
            counter += 1
        return head
