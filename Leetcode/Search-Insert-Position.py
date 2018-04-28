class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) % 2 == 0:
            mid_num = nums[len(nums)/2]
            if mid_num == target:
                return len(nums)/2
            while mid_num != target:
                if mid_num < target:
                    nums.pop()
                else:
                    
                
        else:
            pass
