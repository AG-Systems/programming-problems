class Solution:
    def numDecodings(self, s: str) -> int:
        
        def helper(s, index, cache):
            if index == 0:
                return 1
            starting_index = len(s) - index
            if s[starting_index] == "0":
                return 0
            if index in cache:
                return cache[index]
            
            result = helper(s, index - 1, cache)
            if index >= 2 and int(s[starting_index:starting_index + 2]) <= 26:
                result += helper(s, index - 2, cache)
            cache[index] = result
            return result
        
        return helper(s, len(s), {})
