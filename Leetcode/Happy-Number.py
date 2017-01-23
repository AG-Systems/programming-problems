class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        container = []
        s = str(n)
        for x in range(0,len(s)):
            container.append(int(s[x]))
        counter = 0
        while counter < 40:
            result = 0
            for z in range(0,len(container)):
                result += container[z]** 2 
            print(result)
            if result == 1:
                return True
            else:
                counter += 1
            container = []
            s = str(result)
            for x in range(0,len(s)):
                container.append(int(s[x]))
        return False
