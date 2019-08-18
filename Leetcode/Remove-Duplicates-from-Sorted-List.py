# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        current_node = head
        peek_node = head.next
        
        while current_node.next != None:
            if current_node.val == peek_node.val:
                while peek_node != None and current_node.val == peek_node.val:
                    peek_node = peek_node.next

                current_node.next = peek_node

                if peek_node == None or peek_node.next == None:
                    return head
                
                current_node = current_node.next
                peek_node = peek_node.next
            else:
                current_node = current_node.next
                peek_node = peek_node.next
        return head
