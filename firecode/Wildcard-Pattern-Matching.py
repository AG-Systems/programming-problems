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
