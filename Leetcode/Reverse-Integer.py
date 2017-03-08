class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = list(str(x))
        if s[0] == "-":
            s = s[::-1]
            del s[-1]
            s.insert(0,"-")
        else:
            s = s[::-1]
        r = ''.join(map(str, s))
        return int(r)
