from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = sum([map(list, combinations(nums, i)) for i in range(len(nums) + 1)], [])
        return output
