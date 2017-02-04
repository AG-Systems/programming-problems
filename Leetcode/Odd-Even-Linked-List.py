# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counter = 0
        container = []
        r = []
        while head:
            counter += 1
            if counter % 2 == 0:
                r.append(head.val)
            else:
                container.append(head.val)
            head = head.next
        container.extend(r)
        return container
            
