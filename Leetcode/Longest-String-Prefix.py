class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        highest = ord(s[0]) #97 for A, 122 for Z
        #st = "".join(sorted(s))
        for x in range(0,len(s)):
            if ord(s[x]) >= highest:
                counter += 1
                highest = ord(s[x])
        return counter
