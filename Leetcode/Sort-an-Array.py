class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left, right):
            left_index = 0
            right_index = 0
            sorted_array = []
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    sorted_array.append(left[left_index])
                    left_index += 1
                else:
                    sorted_array.append(right[right_index])
                    right_index += 1
            
            while left_index < len(left):
                sorted_array.append(left[left_index])
                left_index += 1
            
            while right_index < len(right):
                sorted_array.append(right[right_index])
                right_index += 1
            
            return sorted_array
        
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            pivot = int(len(nums) / 2)
            left = merge_sort(nums[0:pivot])
            right = merge_sort(nums[pivot:])
            return merge(left, right)
        
        return merge_sort(nums)
        
