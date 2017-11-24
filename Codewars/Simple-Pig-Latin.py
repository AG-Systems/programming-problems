def pig_it(text):
    #your code here
    res = ""
    text = text.split()
    for x in text:
        if len(x) > 1:
            res += x[1:len(x)]
            res += x[0]
            res += "ay"
            if x != text[-1]:
                res += " "
        else:
            res += x
    return res
    
    
    """
    def pig_it(text):
    #your code here
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    text = text.split(" ")
    new = []
    
    for i in range(len(text)):
        if text[i] in alpha and len(text[i]) == 1:
            text[i] = text[i]+ "ay"
            
        elif len(text[i]) >= 2:
            text[i] = text[i][1: -1]+ text[i][-1]+  text[i][0]+ "ay"
        
        else: text[i] = text[i]
        new.append(text[i])
        
    return " ".join(new)
    """
