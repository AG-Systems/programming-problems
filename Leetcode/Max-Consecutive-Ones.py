class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = 0
        temp = 0
        for x in range(0,(len(nums))):
            if nums[x] == 1:
                temp += 1
            if nums[x] == 0:
                temp = 0
            if temp > maxnum:
                maxnum = temp
        return maxnum
                
        
