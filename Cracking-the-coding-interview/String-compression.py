def stringcompression(string):
    s = ""
    counter = 0
    index = 0
    for x in range(0,len(string)-1):
        if string[x] == string[x+1]:
            counter += 1
        else:
            s+= string[x]
            s+= str(counter+1)
            counter = 0
            index = x
    if counter > 0:
        s+= string[index+1]
        s+= str(counter)
    if len(s) > len(string):
        return string
    else:
        return s

print(stringcompression("aabcccccaaaa"))
