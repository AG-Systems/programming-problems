class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        postfix = [None] * len(nums)
        output = [None] * len(nums)

        prefix[0] = nums[0]
        for current_index in range(1, len(nums)):
            prefix[current_index] = prefix[current_index - 1] * nums[current_index]
        postfix[-1] = nums[-1]
        for current_index in reversed(range(0, len(nums) - 1)):
            postfix[current_index] = postfix[current_index + 1] * nums[current_index]
        # print(prefix, postfix)

        output[0] = 1 * postfix[1]
        output[-1] = 1 * prefix[-2]
        for num in range(1, len(nums) - 1):
            output[num] = prefix[num - 1] * postfix[num + 1]
        return output
