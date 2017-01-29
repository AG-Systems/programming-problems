class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = -1
        m = -1
        nums.sort()
        for x in range(0,len(nums)):
            counter += 1
            if counter != nums[x]:
                m = nums[x]
                return m-1
        if m == -1:
            return len(nums)
