class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        counter = 0
        l = list(itertools.combinations(nums, 2))
        for x in l:
            counter += bin(x[0]^x[1]).count("1")
        return counter
