class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for x in range(0, len(nums) - 2):
            if x == 0 or nums[x] > nums[x - 1]:
                start = x + 1
                end = len(nums) - 1
                
                while start < end:
                    if nums[x] + nums[start] + nums[end] == 0:
                        results.append([nums[x], nums[start], nums[end]])
                    
                    if nums[x] + nums[start] + nums[end] < 0:
                        current_start = nums[start]
                        while current_start == nums[start] and start < end:
                            start += 1
                    else:
                        current_end = nums[end]
                        while current_end == nums[end] and start < end:
                            end -= 1
        return results
        
