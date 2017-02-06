class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        container = {}
        r = []
        counter = 0
        z = 0
        for x in nums:
            if x in container:
                container[x] = target-x
            else:
                container[x] = target-x
        for key,val in container.items():
            if val in container.keys():
                counter = container[val]
                z = val
                break
        r = [nums.index(counter),nums.index(z)]
        return r
        
