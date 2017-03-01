class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        charcounter = {}
        for x in s:
            if x in charcounter:
                charcounter[x] += 1
            else:
                charcounter[x] = 1
        for x in s:
            if charcounter[x] == 1:
                return index
            index += 1
        return -1
