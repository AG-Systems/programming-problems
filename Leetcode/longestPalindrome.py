class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        checker = True
        characters = {}
        for z in s:
            if z in characters:
                characters[z] +=1
            else:
                characters[z] = 1
        for x in characters.values():
            if int(x) % 2 == 0:
                counter += int(x)
            else:
                if checker:
                    checker = False
                    counter += int(x)
        return counter
            
            
