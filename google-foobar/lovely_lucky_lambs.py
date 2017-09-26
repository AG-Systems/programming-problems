def fib_to(n):
     fibs = [0, 1]
     for i in range(2, n+1):
         fibs.append(fibs[-1] + fibs[-2])
     #fibs.remove(0)
     return sum(fibs)
def answer(total_lambs):
    print("LAMBS: " + str(total_lambs))
    import math
    counter = 0
    if total_lambs == 0:
        return 0
    while counter <= 1000000000:
        if fib_to(counter) > total_lambs:
            break
        else:
            res = counter
        counter += 1
    s = res
    #g = (math.log(1 + total_lambs)) / math.log(2)
    #g = int(g)
    gen = [1,2,4]
    total_lambs = total_lambs - sum(gen)
    while total_lambs > 0:
        n1 = gen[-1]
        n2 = gen[-2]
        n3 = gen[-3]
        mul = n1 * 2
        if mul > total_lambs:
            summ = sum(gen)
            x = total_lambs - summ
            if x > (n1 + n2):
                gen.append(x)
                total_lambs = total_lambs - (x)
            else:
                break
        else:
            print(total_lambs, mul)
            gen.append(mul)
            total_lambs = total_lambs - mul
    g = len(gen)
    print(gen)
    print(s, g)
    return abs(s - g)

print(answer(10))
