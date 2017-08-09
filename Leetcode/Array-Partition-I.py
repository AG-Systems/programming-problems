class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = int(len(nums) / 2)
        nums.sort(reverse=True)
        nums = zip(nums,nums[1:])[::2]
        container = []
        for x in nums:
            container.append(min(x))
        return sum(container)
