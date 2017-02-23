class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        container = []
        if len(nums) < 3:
            if len(nums) == 0:
                return nums
            if len(nums) == 1:
                container.append("Gold Medal")
                return container
            else:
                if nums[0] == max(nums):
                    container.append("Gold Medal")
                    container.append("Silver Medal")
                else:
                    container.append("Silver Medal")
                    container.append("Gold Medal")
                return container
        newlist = list(nums)
        newlist.sort()
        newlist = newlist[::-1]
        for x in xrange(len(nums)):
            if nums[x] == newlist[0]:
                container.append("Gold Medal")
            if nums[x] == newlist[1]:
                container.append("Silver Medal")
            if nums[x] == newlist[2]:
                container.append("Bronze Medal")
            if nums[x] != newlist[0] and nums[x] != newlist[1] and nums[x] != newlist[2]:
                pos = newlist.index(nums[x])
                container.append(str(pos+1))
        return container
        
