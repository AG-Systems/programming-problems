class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 0:
            if num == 1:
                return True
            if num % 4 != 0:
                return False
            else:
                num = num / 4
        return False
