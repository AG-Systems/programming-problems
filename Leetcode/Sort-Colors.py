class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        runner = True
        while runner:
            checker = True
            for x in range(0,(len(nums)-1)):
                if nums[x] > nums[x+1]:
                    temp = nums[x]
                    nums[x] = nums[x+1]
                    nums[x+1] = temp
                    checker = False
            if checker == True:
                return None
            
            
                
            
            
                
                
