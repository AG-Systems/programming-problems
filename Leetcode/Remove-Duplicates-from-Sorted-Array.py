class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        k = 0
        
        for x in range(1, len(nums)):
            if nums[x] != nums[k]:
                k += 1
                nums[k] = nums[x]
        
        return k + 1
