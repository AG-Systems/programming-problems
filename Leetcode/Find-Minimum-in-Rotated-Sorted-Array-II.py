class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums) easy joke solution
        min_n = nums[0]
        nums = set(nums)
        for x in nums:
            if x < min_n:
                min_n = x
        return min_n
