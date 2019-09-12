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
        
 """
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return ""
        s = list(s)
        vowel_list = {"a", "e", "o", "u", "i", "A", "E", "O", "U", "I"}
        
        left_ptr = 0
        right_ptr = len(s) - 1
        
        while left_ptr < right_ptr:
            if s[left_ptr] in vowel_list and s[right_ptr] in vowel_list:
                temp = s[left_ptr]
                s[left_ptr] = s[right_ptr]
                s[right_ptr] = temp
                right_ptr -= 1
                left_ptr += 1
            else:
                if s[left_ptr] in vowel_list:
                    right_ptr -= 1
                elif s[right_ptr] in vowel_list:
                    left_ptr += 1
                else:
                    left_ptr += 1
                    right_ptr -= 1
        
        return "".join(s)
"""
