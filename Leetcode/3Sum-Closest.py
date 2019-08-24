class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        results = []
        for x in range(0, len(nums)):
            if x != 0 and nums[x] == nums[x - 1]:
                continue  
            
            left = x + 1
            right = len(nums) - 1
            
            while left < right:
                total_sum = nums[left] + nums[right] + nums[x]
                
                if total_sum == target:
                    return total_sum
                elif total_sum < target:
                    results.append(total_sum)
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                else:
                    results.append(total_sum)
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return min(results, key=lambda x:abs(x-target))
