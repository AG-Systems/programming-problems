class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s.sort()
        g.sort()
        container = []
        index_s = 0
        index_g = 0
        while index_g < len(g):
            if not s[index_s] >= g[index_g]:
                if index_s < len(s):
                    index_s += 1
            else:
                if index_s < len(s):
                    index_s += 1
                container.append(g[index_g])
                index_g += 1
            if index_s >= len(s):
                break
        return len(container)
                
                
                    

                
