class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        letter_table = {}
        for letter in A[0]:
            if letter in letter_table:
                letter_table[letter]["max_counter"] += 1
            else:
                letter_table[letter] = {
                    "key": letter,
                    "counter": 0,
                    "max_counter": 1,
                    "seen": False
                }                
        
        for word in A[1:]:
            for letter in word:
                if letter in letter_table:
                    letter_table[letter]["seen"] = True
                    letter_table[letter]["counter"] += 1
            for key in list(letter_table):
                if letter_table[key]["seen"] and letter_table[key]["counter"] == letter_table[key]["max_counter"]:
                    letter_table[key]["seen"] = False
                    letter_table[key]["counter"] = 0
                else:
                    if letter_table[key]["counter"] == 0:
                        del letter_table[key]
                    else:
                        if letter_table[key]["counter"] < letter_table[key]["max_counter"]:
                            letter_table[key]["max_counter"] = letter_table[key]["counter"]
                        letter_table[key]["counter"] = 0
        
        output = []
        for key,val in letter_table.items():
            if val["max_counter"] == 1:
                output.append(key)
            else:
                for x in range(val["max_counter"] - val["counter"]):
                    output.append(key)
        return output
        
