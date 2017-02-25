class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for x in range(0,len(nums)):
            if nums[x] == target:
                return True
        return False
