class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        else:
            nums = list(set(nums))
            if len(nums) > 2:
                for x in xrange(2):
                    nums.remove(max(nums))
                return max(nums)
            else:
                return max(nums)                
