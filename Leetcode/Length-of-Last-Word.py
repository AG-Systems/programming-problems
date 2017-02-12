class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        container = list(s)
        container = container[::-1]
        ischar = False
        print(container)
        for x in range(0,len(container)):
            if container[x] != " ":
                counter += 1
                ischar = True
            else:
                if x > 0 and ischar:
                    return counter
        return counter

            
