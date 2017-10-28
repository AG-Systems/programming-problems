class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle in haystack:
            return -1
        else:
            return haystack.index(needle)
