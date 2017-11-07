class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = 0
        for x in range(0,len(nums)-1):
            if nums[x] > nums[x+1]:
                counter += 1
        if counter <= 1:
            if len(nums[0:(nums.index(min(nums)))]) > 1:
                return False
            else:
                return True
        else:
            return False
