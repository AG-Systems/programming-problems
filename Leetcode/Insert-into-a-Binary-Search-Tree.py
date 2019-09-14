# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root

    """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        
        def helper(root, val):
            if root == None:
                root = TreeNode(val)
            else:
                if root.val < val:
                    if root.right == None:
                        root.right = TreeNode(val)
                    else:
                        helper(root.right, val)
                else:
                    if root.left == None:
                        root.left = TreeNode(val)
                    else:
                        helper(root.left, val)
        helper(root, val)
        return root
"""
