def answer(n,b):
    #n string
    #b int
    container = []
    k = len(n)
    counter = 0
    #n = str(int(n,b))
    while counter <= 100:
        new_n = [int(i) for i in n]
        x = list(new_n)
        y = list(new_n)
        x.sort(reverse=True)
        y.sort()
        if len(x) < k:
            while len(x) < k:
                x.append(0)
        if len(y) < k:
            y.insert(0,"0")
            while len(y) < k:
                y.insert(0,0)

        x = x[0:k]
        x = ''.join(str(e) for e in x)
        y = y[0:k]
        y = ''.join(str(e) for e in y)
        print(x,y)
        z = int(x) - int(y)
        if len(str(z)) < k:
            lk = list(str(z))
            while len(lk) < k:
                lk.insert(0,"0")
            print(lk)
            lk = ''.join(str(e) for e in lk)
        #z = int(str(z),b)
        print(z)
        if not str(z) in container:
            container.append(str(z))
        else:
            last_num = container.index(str(z))
            print(container, last_num)
            return len(container) - last_num
        n = str(z)
        counter = counter + 1
    print(container)
    print()
    print(set(container))
    
print(answer("1211", 10))
