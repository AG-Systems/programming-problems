class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = {}
        counter = 0
        index = []
        for x in nums:
            if x in container:
                 container[x] += 1
                 if container[x] > 2:
                     index.append(counter)
            else:
                container[x] = 1
            counter += 1
        counter = 0
        for x in index:
            del nums[x-counter]
            counter += 1
        return len(nums)
