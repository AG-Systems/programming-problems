def toJadenCase(string):
    j = ""
    j += string[0].upper()
    for x in range(1,len(string)): 
        if string[x-1] == " ":
            j += string[x].upper()
        else:
            j += string[x]
    return j
