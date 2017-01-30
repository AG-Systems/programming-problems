class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        container = {}
        r = ""
        for x in s:
            if x in container:
                container[x] += 1
            else:
                container[x] = 1
        for x in range(0,len(s)):
            try:
                max_key = max(container, key=lambda k: container[k])
            except:
                break
            for c in range(0,container[max_key]):
                r += str(max_key)
                container[max_key] -= 1
            del container[max_key]
        return r
