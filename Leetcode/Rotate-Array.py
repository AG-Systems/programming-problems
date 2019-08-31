class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
            return None
        
        while k > 0:
            first_el = nums.pop()
            nums.insert(0,first_el)
            k -= 1
