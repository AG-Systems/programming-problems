class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s == s[::-1]:
            return True
        
        def is_palin(s, start, tail):
            while start < tail:
                if s[start] != s[tail]:
                    return False
                start += 1
                tail -= 1
            return True
        
        start = 0
        tail = len(s) - 1
        while start < tail:
            if s[start] != s[tail]:
                return is_palin(s, start + 1, tail) or is_palin(s, start, tail - 1)
            start += 1
            tail -= 1
        return True
            
            
