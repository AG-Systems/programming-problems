class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 0:
            return num
        while len(str(num)) != 1:
            num = map(int, list(str(num)))
            num = sum(num)
        return num
