class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s.replace(" ", "")
        s = s.lower()
        if str(s) == str(s)[::-1]:
            return True
        else:
            return False
