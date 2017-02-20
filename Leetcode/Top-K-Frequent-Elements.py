from collections import OrderedDict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        container = []
        hasht = {}
        counter = 0
        firstnum = False
        while counter < len(nums):
            x = nums[counter]
            if x in hasht:
                hasht[x] += 1
            else:
                hasht[x] = 1
            counter += 1
        counter = 0
        keys = []
        values = []
        for key,val in hasht.items():
            keys.append(key)
            values.append(val)
        for x in range(0,k):
            maxnum = max(values)
            index = values.index(maxnum)
            container.append(keys[index])
            del keys[index]
            del values[index]
        return container
            
