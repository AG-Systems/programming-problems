class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        container = []
        nums.sort()
        nums = nums[::-1]
        counter = len(nums) - k
        for x in range(counter):
            summed = float(sum(nums[0:len(nums)-x]))
            temp = summed / len(nums)
            container.append(temp)
        print container
