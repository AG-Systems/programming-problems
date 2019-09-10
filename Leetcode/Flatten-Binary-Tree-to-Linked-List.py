# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        
        self.dfs_list = []
        
        def dfs(root):
            if root:
                self.dfs_list.append(root)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        root = self.dfs_list.pop(0)
        while self.dfs_list:
            node = self.dfs_list.pop(0)
            root.right = node
            root.left = None
            root = root.right
        return root

    """
    SOLUTION THAT I SHOULD AIM FOR!!!!
    
    def flatten(self, root: TreeNode) -> None:
        # put right subtree to the left subtree's right-most
        # put left subtrees to the right
        # go to right subtrees and repeat
        if not root:
            return
        node = root.left
        if node:
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)
"""
