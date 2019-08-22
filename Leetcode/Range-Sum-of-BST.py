# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        
        self.answer = 0
        def sum_tree(root, L, R):
            if root:
                if L <= root.val <= R:
                    self.answer += root.val
                sum_tree(root.left, L, R)
                sum_tree(root.right, L, R)
        sum_tree(root, L, R)
        
        return self.answer
        
