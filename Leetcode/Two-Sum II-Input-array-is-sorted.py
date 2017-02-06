class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        y = len(numbers)-1
        container = []
        while x < y:
            result = numbers[x] + numbers[y]
            if result == target:
                container = [x+1,y+1]
                return container
            if result > target:
                y -= 1
            if result < target:
                x += 1
