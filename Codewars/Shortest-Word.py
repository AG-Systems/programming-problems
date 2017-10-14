def find_short(s):
    link = s.split(" ")
    smallest_word = float('Inf')
    for x in range(0, len(link)):
        if len(link[x]) < smallest_word:
            l = len(link[x])
            smallest_word = l
    return l # l: shortest word length
