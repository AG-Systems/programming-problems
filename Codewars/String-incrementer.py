def increment_string(string):
    if string[-1].isalpha():
        return string + "1"
    for x in range(len(string)):
        val = string[x]
        if val.isdigit():
            num = int(string[x:-1])
        
    string = string[0:(len(string) - len(str(num)))] + str(int(num + 1))
    return string
