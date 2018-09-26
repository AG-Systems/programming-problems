# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue1 = [p]
        queue2 = [q]
        
        while queue1 and queue2:
            node1 = queue1.pop()
            node2 = queue2.pop()
            if not node1 and not node2:
                continue
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
            if node1.val != node2.val:
                return False
            queue1.append(node1.left)
            queue1.append(node1.right)
            
            queue2.append(node2.left)
            queue2.append(node2.right)
        return len(queue1) == len(queue2)
            
