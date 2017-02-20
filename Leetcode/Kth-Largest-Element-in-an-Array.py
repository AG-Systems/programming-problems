class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return k
        for x in range(1,k):
            index = nums.index(max(nums))
            del nums[index]
        return max(nums)
        
