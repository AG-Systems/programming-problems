def match(first, second):
    if len(first) == len(second) and ("?" in first  or "*" in first):
        return True
    if len(first) > len(second) and "*" in first and not "?" in first:
        return True
    star = 0
    ques = 0
    first = list(first)
    second = list(second)
    for x in first:
        if x == "*" and "?" not in first:
            star = first.index(x)
            for z in range(len(second) - len(first)+1):
                first.insert(star, "*")
            if len(first)-len(second) == 1:
                first.remove("*")
        elif x == "*" and "?" in first:
            star = first.index(x)
            char1 = first.index(first[star+1])
            if first[star+1] != "*":
                char2 = second.index(first[star+1])
                if len(first[char1:-1]) == len(second[char2:-1]) and not "*" in first[char1:-1] and "?" in first[char1:-1]:
                    return False
            for z in range((len(second) - len(first) - first.count("?"))+1):
                first.insert(star, "*")
            if len(first)-len(second) == 1:
                first.remove("*")
            
    if len(first) == len(second):
        print(first,second)
        return True
    else:
        print(first,second)
        return False

#print(match("fi*de", "firecode")) #True
#print(match("fir?code", "firecode")) #True
#print(match("fi*d?", "firecode")) #true
print(match("fi*d?", "firecodee")) #False
#print(match("fi?de", "firecode")) #False
#print(match("*i*d?", "fabfirecode")) #True
#print(match("?i?e*d?", "fairecode")) #False
print(match("*i?e*d?", "firecode")) #True

    
    """
    
    
    def match(first, second):
    l = 0; m = 0; starIdx = -1;i = -1;
    while l < len(second):
        if m < len(first) and (first[m] == '?' or first[m] == second[l]) :
            m += 1
            l += 1
        elif m < len(first) and first[m] == '*' :  
            i = l
            starIdx = m 
            m += 1 
        elif starIdx != -1 :
            l = i+1
            m = starIdx + 1
            i += 1
        else :
            return False
    while m < len(first) and first[m] == '*':
        m += 1
    return m == len(first)
    
"""
