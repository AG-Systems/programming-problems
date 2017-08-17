class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        container = {}
        for x in s:
            if x in container:
                container[x] += 1
            else:
                container[x] = 1
        for x in t:
            if x not in container:
                return x
            else:
                container[x] -= 1
                if container[x] < 0:
                    return x
                
