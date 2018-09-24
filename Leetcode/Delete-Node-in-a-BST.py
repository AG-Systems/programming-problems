# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            smallestNode_in_right = self.findsmallest(root.right)
            if not smallestNode_in_right:   
                return root.left
            smallestNode_in_right.left = root.left
            return root.right            
    def findsmallest(self, root):
        if root == None:
            return None
        while root.left:
            root = root.left
        return root
