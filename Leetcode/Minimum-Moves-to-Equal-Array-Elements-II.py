class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        counter = [0]
        nums.sort()
        mid = []
        if len(nums) % 2 == 0:
            mid.append(nums[len(nums) / 2])
            if len(nums) > 2:
                mid.append(nums[(len(nums) / 2) + 1])
        else:
            mid.append(nums[len(nums)/ 2])
        for x in nums:
            if x != mid[0]:
                counter[0] += abs(x - mid[0])
        if len(mid) > 1:
            counter.append(0)
            for x in nums:
                if x != mid[1]:
                    counter[1] += abs(x - mid[1])
        return min(counter)
