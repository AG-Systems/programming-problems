class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s = ""
        container = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) >= len(num2):
            size = len(num1)
        else:
            size = len(num2)
        if len(num1) == 1 and len(num2) == 1:
            temp = 0
            temp += int(num1[0])
            temp += int(num2[0])
            s += str(temp)
            return s
        counter = False
        for z in range(0, size):
            if counter:
                temp = 1
            else:
                temp = 0
            if z < len(num1):
                temp += int(num1[z])
            if z < len(num2):
                temp += int(num2[z])
            if temp < 10:
                container.append(temp)
                counter = False
            else:
                counter = True
                lastdigit = int(repr(temp)[-1])
                container.append(lastdigit)
        container = container[::-1]
        if container[0] == 0:
            container.insert(0,1)
        for x in range(0,len(container)):
            s += str(container[x])
        return s
