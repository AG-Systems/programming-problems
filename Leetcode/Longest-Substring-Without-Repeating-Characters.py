class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        longest_substring = 1
        substring_set = set()
        
        index = 0
        while index < len(s):
            if s[index] not in substring_set:
                seeker = index + 1
                substring_set.add(s[index])
                while seeker < len(s) and s[seeker] not in substring_set:
                    substring_set.add(s[seeker])
                    seeker += 1
                longest_substring = max(longest_substring, seeker - index)
                substring_set.clear()
                index += 1
            else:
                index += 1
        return longest_substring
