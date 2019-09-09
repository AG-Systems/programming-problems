# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        def check(node, left_limit, right_limit):
            if node == None:
                return True
            
            if left_limit < node.val < right_limit:
                return check(node.left, left_limit, node.val) and check(node.right, node.val, right_limit)
            return False
        return check(root, -1*float("inf"), float("inf"))
    
"""
        if root == None:
            return True
        
        def is_bst_helper(root, left_val, right_val):
            if root == None:
                return True
            
            if root.val <= left_val or root.val >= right_val:
                return False
            
            return is_bst_helper(root.left, left_val, root.val) and is_bst_helper(root.right, root.val, right_val)
        
        return is_bst_helper(root, float("-inf"), float("inf"))
"""
