# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        container = []
        sum = 0
        container.append(root)
        while container:
            for x in range(0, len(container)):
                node = container.pop(0)
                if node.left:
                    container.append(node.left)
                    if node.left.left == None:
                        if node.left.right == None:
                            sum += node.left.val
                if node.right:
                    container.append(node.right)
        return sum
            
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.answer = 0
        def leaf_sigma(root):
            if root == None:
                return 0
            
            left = root.left
            if left and not left.left and not left.right:
                self.answer += left.val
            leaf_sigma(root.left)
            leaf_sigma(root.right)
            
        leaf_sigma(root)
        return self.answer
"""




"""
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
"""
