def reversewords(s):
    container = []
    s = s.split(" ")
    z = ""
    for x in s:
        container.append(x)
    container = container[::-1]
    for x in range(0,len(container)):
        z += str(container[x])
        z += " "
    return z

print(reversewords("Hello this is max"))
