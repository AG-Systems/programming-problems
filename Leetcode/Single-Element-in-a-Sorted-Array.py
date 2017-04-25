class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = {}
        for x in nums:
            if x in container:
                container[x] += 1
            else:
                container[x] = 1
        for key,val in container.items():
            if container[key] == 1:
                return key
