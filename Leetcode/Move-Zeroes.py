class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = 0
        nonzero = -1
        while counter < len(nums):
            if nums[counter] != 0:
                nonzero += 1
                if nonzero < counter:
                    nums[nonzero] = nums[counter]
                    nums[counter] = 0
            counter += 1

"""
class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) == 0:
            return
        
        index = 0
        for digit in nums:
            if digit != 0:
                nums[index] = digit
                index += 1
        
        
        for zero in range(index, len(nums)):
            nums[zero] = 0
        return
"""
                
                
            
        
            
