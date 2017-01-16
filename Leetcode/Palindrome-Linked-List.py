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
        
        
