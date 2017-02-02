class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = {}
        for x in nums:
            if x in container:
                container[x] += 1
                if container[x] > 1:
                    return x
            else:
                container[x] = 1
