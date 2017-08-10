class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float("inf")
        min2 = float("inf")
        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")
        
        for x in nums:
            if x <= min1:
                min2 = min1
                min1 = x
            elif x <= min2:
                min2 = x
            
            if x >= max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x >= max2:
                max3 = max2
                max2 = x
            elif x >= max3:
                max3 = x
        return max(min1 * min2 * max1, max1 * max2 * max3)
            
