def rotLeft(a, d):
    while d > 0:
        val = a.pop(0)
        a.append(val)
        d -= 1
