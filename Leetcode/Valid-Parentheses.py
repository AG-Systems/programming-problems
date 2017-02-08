class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        container = []
        for x in range(0,len(s)):
            if s[x] == '(' or s[x] == '[' or s[x] == '{':
                container.append(s[x])
            if s[x] == ")":
                if container == [] or container.pop() != "(":
                    return False
            if s[x] == "]":
                if container == [] or container.pop() != "[":
                    return False
            if s[x] == "}":
                if container == [] or container.pop() != "{":
                    return False
        if len(container) == 0:
            return True
        else:
            return False
