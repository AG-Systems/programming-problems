# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if not root.left and not root.right:
            return 0
        self.node_val_list = set()
        
        def helper(root):
            if root == None:
                return None
            self.node_val_list.add(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        self.node_val_list = sorted(self.node_val_list)
        if len(self.node_val_list) == 1:
            return 0
        
        min_val_difference = float("inf")
        for index in range(0, len(self.node_val_list) - 1):
            num_1 = self.node_val_list[index]
            num_2 = self.node_val_list[index + 1]
            diff = abs(num_1 - num_2)
            if diff < min_val_difference:
                min_val_difference = diff
        return min_val_difference
        
