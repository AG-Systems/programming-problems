class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_counter = {}
        for letter in sentence:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1
        
        return len(letter_counter.keys()) == 26
