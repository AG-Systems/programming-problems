# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxnum = max(nums)
        pivot = nums.index(maxnum)
        left = nums[:pivot]
        right = nums[pivot+1:]
        node = TreeNode(maxnum)
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node
        
            
            
        
            
            
            
        
