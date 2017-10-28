class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif len(needle) > len(haystack):
            return -1
        elif needle not in haystack:
            return -1
        else:           
            counter = 0
            current_char = needle[counter]
            index = -1
            x = 0
            while x < len(haystack):
                print(current_char,haystack[x], index, x)
                if current_char == haystack[x]:
                    counter += 1
                    if counter == 1:
                        index = x
                    if counter >= len(needle):
                        return index
                    current_char = needle[counter]
                else:
                    x = x - counter
                    counter = 0
                    current_char = needle[counter]
                    index = -1
                x = x + 1
            return index
    """
    if not needle in haystack:
        return -1
    else:
        return haystack.index(needle)
    """
                
