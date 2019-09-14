class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = {}
        for x in nums:
            if x in container:
                container[x] += 1
                if container[x] > 1:
                    return x
            else:
                container[x] = 1

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        ptr_1 = nums[0]
        ptr_2 = slow
        while ptr_1 != ptr_2:
            ptr_1 = nums[ptr_1]
            ptr_2 = nums[ptr_2]
        return ptr_1
"""
