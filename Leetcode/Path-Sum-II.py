# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_val: int) -> List[List[int]]:
        if root == None:
            return []
        
        self.path_sum = []
        
        def helper(root, path):
            if root == None:
                return None
            
            if not root.left and not root.right:
                path += [root.val]
                self.path_sum.append(path)
                return

            helper(root.left, path + [root.val])
            helper(root.right, path + [root.val])
            
        helper(root, [])
        
        index = 0
        while index < len(self.path_sum):
            if sum(self.path_sum[index]) != sum_val:
                del self.path_sum[index]
                index = 0
            else:
                index += 1
        return self.path_sum
