class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        replaced_s = [""] * len(s)
        letter_table = {}
        char_set = set()
        for index in range(0, len(s)):
            digit = s[index]
            if not digit in letter_table:
                letter_table[digit] = t[index] 
                if t[index] not in char_set:
                    char_set.add(t[index])
                else:
                    return False
            replaced_s[index] = letter_table[digit]
        replaced_s = "".join(replaced_s)
        return replaced_s == t
