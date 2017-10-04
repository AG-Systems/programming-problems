class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        counter = 0
        #container = []
        for x in range(n+1):
            x = str(x)
            if "1" in x:
                #container.append(int(x))
                counter += x.count("1")
        #print(container)
        return counter
