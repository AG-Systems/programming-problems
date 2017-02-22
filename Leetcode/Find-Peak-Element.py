class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 2:
            for x in range(1,len(nums)-1):
                if nums[x] > nums[x-1] and nums[x] > nums[x+1]:
                    return x
            if nums[-1] > nums[-2]:
                return len(nums)-1
            return 0
        else:
            return nums.index(max(nums))
            
