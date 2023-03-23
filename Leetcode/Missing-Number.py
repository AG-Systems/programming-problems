class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = -1
        m = -1
        nums.sort()
        for x in range(0,len(nums)):
            counter += 1
            if counter != nums[x]:
                m = nums[x]
                return m-1
        if m == -1:
            return len(nums)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_seq_xor = 0
        current_num_xor = 0
        
        x = 0
        while x <= len(nums):
            total_seq_xor ^= x
            x += 1
            
        for x in range(0, len(nums)):
            num = nums[x]
            current_num_xor ^= num
        
        return total_seq_xor ^ current_num_xor
"""


"""
        current_sum = 0
        max_sum = 0

        for i in range(0, len(nums) + 1):
            max_sum += i
        
        for i in nums:
            current_sum += i
        
        return max_sum - current_sum
"""
        
            
        
