class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.saved = list(nums)
        self.numslist = nums
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.saved

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.numslist)
        return self.numslist


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
