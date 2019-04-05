class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = n * -1
            val = x
            while n > 1:
                n -= 1
                val *= x
            return 1 / val
        else:
            val = x
            while n > 1:
                n -= 1
                val *= x
            return val
