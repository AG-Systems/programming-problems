class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = {}
        r = []
        for x in nums:
            if x in container:
                container[x] += 1
            else:
                container[x] = 1
        for key,val in container.items():
            if val == 1:
                return key
