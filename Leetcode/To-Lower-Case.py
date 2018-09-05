class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        #return str.lower()
        
        #abcdefghijklmnopqrstuvwxyz
        alphabet = {
            "A": "a",
            "B": "b",
            "C": "c",
            "D": "d",
            "E": "e",
            "F": "f",
            "G": "g",
            "H": 'h',
            "I": "i",
            "J": "j",
            "K": "k",
            "L": 'l',
            "M": "m",
            "N": "n",
            "O": "o",
            "P": 'p',
            "Q": "q",
            "R": "r",
            "S": "s",
            "T": 't',
            "U": "u",
            "V": "v",
            "W": "w",
            "X": 'x',
            "Y": "y",
            "Z": "z"
        }
        
        lowercasestr = []
        
        for letter in str:
            if letter in alphabet:
                lowercasestr.append(alphabet[letter])
            else:
                lowercasestr.append(letter)
        return ''.join(lowercasestr)
        
