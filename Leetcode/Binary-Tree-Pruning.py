# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val == 1:
            return root
        if root.val == 0 and (root.left == None and root.right == None):
            return None
        return root
        

  """
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
    
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val == 0 and root.left == None and root.right == None:
            root = None
        return root
        
        
 """     
