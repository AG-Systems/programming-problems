class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        container = {}
        if len(s) == 1 and len(t) == 1:
            if s in t:
                return True
            else:
                return False
        if s >= t:
            r = t
            for z in s:
                if z in container:
                    container[z] +=1
                else:
                    container[z] = 1
        else:
            r = s
            for z in t:
                if z in container:
                    container[z] +=1
                else:
                    container[z] = 1   
        for z in range(0,len(container.values())):
            for x in range(0,len(r)):
                if container.keys()[z] == r[x]:
                    container[r[x]] -= 1
        for c in range(0,len(container.values())):
            if container.values()[c] > 0 or container.values()[c] < 0:
                return False
        return True
