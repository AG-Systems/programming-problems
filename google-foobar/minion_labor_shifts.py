def answer(data,n):
    hashmap = {}
    if n == 0:
        return []
    for x in data:
        if x in hashmap:
            hashmap[x] += 1
        else:
            hashmap[x] = 1

    for key, val in hashmap.items():
        if val > n:
            #data.remove(key)
            data = [x for x in data if x != key]
    return data
