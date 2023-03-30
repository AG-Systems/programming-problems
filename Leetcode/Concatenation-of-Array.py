class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        counter = 0
        for i in range(0, len(ans)):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[counter]
                counter += 1
        return ans
