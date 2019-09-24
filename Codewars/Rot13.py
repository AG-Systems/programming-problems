def rot13(message):
    rot_13_string = [""] * len(message)
    # z = 97 - 122
    # capital = 65 - 90
    shift = 13
    for index in range(0, len(message)):
        letter = message[index]
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90:
            is_capital = False
            if letter.isupper():
                is_capital = True
                letter = letter.lower()
            new_letter = ord(letter) - 97
            new_letter += shift
            if new_letter > 26:
                new_letter -= 26
            new_letter += 97
            new_letter = chr(new_letter) 
            if is_capital:
                new_letter = new_letter.upper()
            rot_13_string[index] = new_letter
        else:
            rot_13_string[index] = letter
      
    return "".join(rot_13_string)
