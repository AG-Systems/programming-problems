# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        self.result = True
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if abs(left - right) > 1:
                self.result = False
            return max(left, right) + 1
        
        helper(root)
        return self.result
                
