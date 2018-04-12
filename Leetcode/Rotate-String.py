class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B):
            return False
        a_string = list(A)
        for x in range(0,len(a_string)-1):
            left_char = a_string[0]
            a_string.pop(0)
            a_string.append(left_char)
            if a_string == list(B):
                return True
        return False
