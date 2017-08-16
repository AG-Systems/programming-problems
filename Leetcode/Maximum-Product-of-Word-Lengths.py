class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        counter = 0
        while words:
            current_word = set(words[0])
            current_length = len(words[0])
            words = words[1:]
            #print current_word, current_length, words
            for x in words:
                for char in current_word:
                    if char in x:
                        break
                else:
                    counter = max(counter, current_length * len(x))
        return counter
