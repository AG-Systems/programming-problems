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
        
        is_duplicates_table = {}
        current_node = head
        while current_node:
            if current_node.val in is_duplicates_table:
                is_duplicates_table[current_node.val] = True
            else:
                is_duplicates_table[current_node.val] = False
            current_node = current_node.next

        current_node = head
        if is_duplicates_table[current_node.val]:
            while is_duplicates_table[current_node.val]:
                current_node = current_node.next
                if not current_node:
                    return None
            head = current_node
        peek_node = current_node.next
        
        while peek_node != None:
            if is_duplicates_table[peek_node.val]:
                while peek_node and is_duplicates_table[peek_node.val]:
                    peek_node = peek_node.next
                current_node.next = peek_node
                if not peek_node:
                    return head
                
            current_node = current_node.next
            peek_node = peek_node.next
        return head
            
        
                 
