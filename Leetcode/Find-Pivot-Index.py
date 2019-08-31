class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1 or not nums:
            return -1
        
        left = 0
        right = sum(nums[1:])
        pivot = 0
        while left != right and pivot < len(nums) - 1:
            pivot += 1
            left += nums[pivot - 1]
            right -= nums[pivot]
        
        if left != right:
            return -1
        else:
            return pivot
        
