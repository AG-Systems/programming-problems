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
