def match(first, second):
    if len(first) == len(second) and "?" in first and not "*" in second:
        return True
    if "*" in first and not "?" in first:
        l = []
        for x in range(len(first)):
            if first[x] != "*":
                l.append(first[x])
            else:
                if l != []:
                    index = l.index(l[-1])
                    temp = ["*"] * int(len(second[index:index+1]))
                    l.extend(temp)
                else:
                    l.append("*")
        if len(l) == len(second):
            return True
        else:
            return False
    if "*" in first and "*" in first:
        pass

    
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
