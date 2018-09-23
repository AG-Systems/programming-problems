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
