class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        container = {}
        indices = []
        for x in nums:
            if x in container:
                container[x] = target-x
            else:
                container[x] = target-x
        for key,val in container.items():
            if val in nums:
                indices.append(nums.index(key))
                if key != val:
                    indices.append(nums.index(val))
                else:
                    nums[nums.index(key)] = -99
                    indices.append(nums.index(val))
                break
        return indices
