class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(bin(num))
        r = ""
        container = []
        checker = False
        for x in range(0,len(s)):
            if s[x] == '0' and checker:
                container.append(1)
            if s[x] == '1' and checker:
                container.append(0)
            if s[x] != '0' and s[x] != '1':
                checker = True
        for z in range(0,len(container)):
            r += str(container[z])
        return int(r, 2)
            
            
