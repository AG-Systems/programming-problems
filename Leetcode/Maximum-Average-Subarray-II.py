class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        import math
        container = []
        sort_list = list(nums)
        sort_list.sort()
        sort_list = sort_list[::-1]
        for x in range(1, len(sort_list)):
            num1 = nums.index(sort_list[x-1])
            num2 = nums.index(sort_list[x])
            temp = nums[num1:num2+1]
            if num2 < num1:
                temp = nums[num2:num1+1] 
            print temp
            if len(temp) >= k:
                container.append(float(sum(temp)) / len(temp))
            else:
                if 0 in nums:
                    checker = False
                    if abs(nums.index(0)-num1) == 1:
                        if num1 > num2:
                            num1 = num1 + 1
                        else:
                            num1 = num1 - 1
                        checker = True
                    elif abs(nums.index(0)-num2) == 1:
                        if num1 > num2:
                            num2 = num2 + 1
                        else:
                            num2 = num2 - 1
                        checker = True
                    temp = nums[num1:num2+1]
                    if num2 < num1:
                        temp = nums[num2:num1+1]
                    if checker:
                        container.append(float(sum(temp)) / len(temp)) 
        if len(container) > 0:
            return max(container)
        else:
            return float(nums[0])
            
            
