class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        container = list(s)
        revvowel = []
        vowellist = ["o","a","u", "e", "i", "O", "A", "U", "E", "I"]
        for x in xrange(len(container)):
            if container[x] in vowellist:
                revvowel.append(container[x])
                container[x] = "-1"
        for x in xrange(len(container)):
            if container[x] == "-1":
                container[x] = revvowel.pop()
        newstring = ''.join(map(str, container))
        return newstring
        
