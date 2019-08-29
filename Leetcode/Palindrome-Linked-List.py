# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        
        current = head
        is_even = length % 2 == 0
        if is_even:
            length = length / 2
        else:
            import math
            length = math.ceil(length / 2)
        
        seeker = head
        reverse_nodes = None
        future = None
        
        counter = 0
        while seeker and length > 0:
            future = seeker.next
            seeker.next = reverse_nodes
            reverse_nodes = seeker
            seeker = future
            length -= 1
        if not is_even:
            seeker = seeker.next

        while reverse_nodes and seeker:
            if reverse_nodes.val != seeker.val:
                return False
            reverse_nodes = reverse_nodes.next
            seeker = seeker.next
        return True
            
            
            
"""        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        node = head
        length = 0
        container = []
        while node:
            container.append(node.val)
            node = node.next
            length += 1
        if length == 0 or length == 1:
            return True
        counter = 0
        for x in range(0,length):
            if container[x] == container[length-1]:
                counter += 1  
        if length - counter >= 1:
            if container[::-1] == container:
                return True
            else:
                return False
        else:
            return True
        
 """       
