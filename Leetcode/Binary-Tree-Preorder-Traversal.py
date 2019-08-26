# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder_list = []
        def dfs(root):
            if root:
                preorder_list.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return preorder_list
