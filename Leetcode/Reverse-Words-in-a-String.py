class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        container = []
        s = s.split(" ")
        z = ""
        for x in s:
            if x != "":
                container.append(x)
        container = container[::-1]
        for c in range(0,len(container)):
            z += str(container[c])
            if len(container) - c > 1:
                z += " "
        print (z)
        return z
