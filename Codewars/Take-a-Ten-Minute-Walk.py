def isValidWalk(walk):
    if len(walk) == []:
        return True
    if len(walk) > 10 or len(walk) < 10:
        return False
    pos_table = {
        "n": 0,
        "s": 0,
        "e": 0,
        "w": 0
    }
    
    for pos in walk:
        pos_table[pos] += 1
    
    if pos_table["n"] == pos_table["s"] and pos_table["e"] == pos_table["w"]:
        return True
    else:
        return False
