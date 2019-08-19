# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return None
        
        vals = []
        def dfs(root):
            if root:
                vals.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)     
        return len(set(vals)) == 1
        
        
        
