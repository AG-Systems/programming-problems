# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        def dfs(root, num):
            if not root:
                return [0]
            new_num = (num * 10 ) + root.val # 4
            if root.left == None and root.right == None:
                return [new_num]
            elif root.left == None:
                return dfs(root.right, new_num)
            elif root.right == None:
                return dfs(root.left, new_num)
            else:
                return dfs(root.left, new_num) + dfs(root.right, new_num)
        
        return sum(dfs(root,0))
