# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1 = []
        number2 = []
        num1 = ""
        num2 = ""
        node = l1
        while l1:
            number1.append(l1.val)
            l1 = l1.next
        while l2:
            number2.append(l2.val)
            l2 = l2.next
        for x in number1:
            num1 += str(x)
        for x in number2:
            num2 += str(x)
        num1 = int(num1)
        num2 = int(num2)
        sumed = num1 + num2
        sumed = list(str(sumed))
        counter = 0
        while counter < len(sumed):
            node.val = int(sumed[counter])
            if node.next:
                node = node.next
            else:
                node.next = ListNode(0)
            counter += 1
        return node
