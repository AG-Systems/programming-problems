def insert_star_between_pairs(a_string, index=0):
    if not a_string or len(a_string) == 1 or index >= len(a_string):
        return a_string
    else:
        if index+1 < len(a_string):
            if a_string[index] == a_string[index+1]:
                l = list(a_string)
                l.insert(index+1, "*")
                a_string = ''.join(l)
                print l
        return insert_star_between_pairs(a_string, index+1)
