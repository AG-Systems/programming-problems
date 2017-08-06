def  decrypt(encrypted_message):
    import math
    key = "8251220"
    og_sentence = ""
    counter = 0
    for x in xrange(len(encrypted_message)):
        capital = False
        if encrypted_message[x].isupper():
            capital = True
        if encrypted_message[x] != " ":
            temp = chr(ord(encrypted_message[x]) - int(key[counter]))
            if ord(temp) > 65 and ord(temp) < 91:
                og_sentence += temp
            else:
                if ord(temp) > 96 and ord(temp) < 123:
                    og_sentence += temp
                else:
                    if ord(temp) < 97 and ord(temp) > 90 and not capital:
                        val = abs((abs(ord(temp) - 97)) - int(key[counter]))
                        temp = chr(ord('z') - (val-4))
                        og_sentence += temp
                    elif capital:
                        val = abs((abs(ord(temp) - 65)) - int(key[counter]))
                        temp = chr(ord('Z') - (val+5))
                        og_sentence += temp                         
                    pass                      
            if counter >= len(key)-1:
                counter = 0
            else:
                counter += 1
        else:
            og_sentence += " "
    return og_sentence
