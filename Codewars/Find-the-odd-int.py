def find_it(seq):
    hashtable = {}
    for x in seq:
        if x in hashtable:
            hashtable[x] += 1
        else:
            hashtable[x] = 1
    for key,val in hashtable.items():
        if val % 2 != 0:
            return key


"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

CLEVER SOLUTION
"""
