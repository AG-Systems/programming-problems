def answer(n, b, link=[]):
    # your code here
    if b == 0:
        print(link)
        if link[-1] == link[-2]:
            return 1
        else:
            #last = link[link[::-1].index(min(link))]
            last = link[-1]
            print(last)
            counter = 2
            while counter < len(link):
                if link[-counter] == last:
                    return counter
                counter += 1
            return len(link)
    k = len(n)
    new_n = [int(i) for i in n]
    x = list(new_n)
    y = list(new_n)
    x.sort(reverse=True)
    y.sort()
    x = int(''.join(str(e) for e in x))
    y = int(''.join(str(e) for e in y))
    #print(x,y)
    z = int(x) - int(y)
    if len(str(z)) == k:
        n = z
    else:
        z = list(str(z))
        z.insert(0, "0")
        z = ''.join(str(e) for e in z)
        n = z
    link.append(z)
    b = b - 1
    return answer(str(n),b, link)
    

print(answer("502212", 10))

