# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            if root.val == sum and not root.left and not root.right:
                return True
            else:
                return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)
        else:
            return False
        
                
            
            
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.has_sum = False
        def dfs(root, sum_path, goal_sum):
            if root:
                sum_path += root.val
                if root.left == None and root.right == None:
                    if sum_path == goal_sum:
                        self.has_sum = True
                        return True                    
                dfs(root.left, sum_path, goal_sum)
                dfs(root.right, sum_path, goal_sum)


        
        dfs(root, 0, sum)
        
        return self.has_sum
"""
