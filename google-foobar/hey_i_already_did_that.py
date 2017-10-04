def based(n, b):
    a = [0] * n
    if n < 0:
        return 0
    if b <= 1:
        return 1
    x = n
    counter = 0
    while n >= b:
        q = n / b
        t = n - q * b
        a[counter] = t
        n = q
        counter += 1
    a[counter] = n
    final_num = ""
    for i in range(counter):
        h = a[counter-i]
        final_num += str(h)
        #print(h)
    #print(a[0])
    #print(b, x)
    #return(counter+1)
    return final_num + str(a[0])
"""
def to_decimal(number, base):
    return sum([int(character) * base ** index for index,character in enumerate(str(number)[::-1])])
"""
def answer(n,b):
    if int(max(n)) > (b-1):
        return 1
    k = len(n)
    print("N is: " + n)
    print("B is: " + str(b))
    print("K: " + str(k))
    counter = 0
    container = []
    print("Started compution")
    while counter < 15:
        new_n = [int(i) for i in n]
        x = list(new_n)
        y = list(new_n)
        x.sort(reverse=True)
        y.sort()
        x = ''.join(str(e) for e in x)
        y = ''.join(str(e) for e in y)
        print(x,y)
        x = int(str(x),b)
        y = int(str(y),b)
        print("X | Y")
        print(x,y)
        z = x - y
        z = int(str(z), 10)
        print("Z: " + str(z))
        z = based(z,b)
        if len(str(z)) == k:
            n = str(z)
        else:
            z = list(str(z))
            while len(z) < k:
                z.insert(0,0)
            z = ''.join(str(e) for e in z)
            n = str(z)
        n = str(z)
        print(n)
        counter += 1
        if n not in container:
            container.append(n)
            if len(container) > 11:
                container.pop(0)
        else:
            last_num = container.index(str(n))
            return len(container) - last_num
        print("Counter: " + str(counter))
    print(container)
    #return len(set(container))
    
print(answer("6050", 3))
