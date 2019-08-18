class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_table = {}
        for character in chars:
            if character in char_table:
                curr_counter = char_table[character]["curr_counter"] + 1
                char_table[character] = {
                    "key": character,
                    "curr_counter": curr_counter,
                    "max_counter": curr_counter
                }
            else:
                char_table[character] = {
                    "key": character,
                    "curr_counter": 1,
                    "max_counter": 1
                }
        sum_of_lengths = 0
        for word in words:
            broken_word = False
            for letter in word:
                if letter not in char_table:
                    broken_word = True
                    break
                else:
                    char_table[letter]["curr_counter"] -= 1
                    if char_table[letter]["curr_counter"] < 0:
                        broken_word = True
                        break
            for letter in word:
                if letter in char_table:
                    char_table[letter]["curr_counter"] = char_table[letter]["max_counter"]
            if not broken_word:
                sum_of_lengths += len(word)
        
        return sum_of_lengths
