class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ") 
        zx = ""
        for x in range(0,len(s)):
            s[x] = s[x][::-1]
        for x in range(0,len(s)):
            if x != len(s)-1:
                zx += s[x]
                zx += " "
            else:
                zx += s[x]
        return zx
                
