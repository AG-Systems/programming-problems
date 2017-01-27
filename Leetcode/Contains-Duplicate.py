class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        container = {}
        for x in nums:
            if x in container:
                container[x] += 1
                if container[x] > 1:
                    return True
            else:
                container[x] = 1
        return False
