def duplicate_items(list_numbers):
    container = {}
    l = []
    for x in list_numbers:
        if x in container:
            l.append(x)
            container[x] += 1
        else:
            container[x] = 1
    l.sort()
    return l
