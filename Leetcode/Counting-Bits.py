class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        container = []
        for x in xrange(num+1):
            container.append(bin(x).count("1"))
        return container
