# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer != None:
            fast_pointer = fast_pointer.next
            if fast_pointer != None:
                fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        return slow_pointer
