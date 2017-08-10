class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        nums.sort()
        nums = nums[::-1]
        neg = 0
        output = 1
        for x in nums:
            if x < 0:
                neg += 1
        if neg == 0:
            nums = nums[0:3]
            for x in nums:
                output *= x
            return output
        elif neg == 1:
            counter = 0
            for x in nums:
                if x > 0:
                    output *= x
                    counter += 1
                if counter >= 3:
                    return output
        elif neg == 2:
            if len(nums) == 3:
                nums = nums[0:3]
                for x in nums:
                    output *= x
                return output
            else:
                negative = abs(sum(nums[-2:]))
                pos = abs(sum(nums[1:3]))
                output = nums[0]
                if pos > negative:
                    for x in nums[1:3]:
                        output *= x
                    return output      
                else:
                    for x in nums[-2:]:
                        output *= x
                    return output                       
        elif neg > 2:
            last2 = nums[-2:]
            output = nums[0] 
            for x in last2:
                output *= x
            return output
            
