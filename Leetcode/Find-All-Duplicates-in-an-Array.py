class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        container = {}
        for x in nums:
            if x in container:
                container[x] += 1
                if container[x] > 1:
                    r.append(x)
            else:
                container[x] = 1
        return r

    
