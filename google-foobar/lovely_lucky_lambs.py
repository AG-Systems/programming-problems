def fib_to(n, total_lambs):
     fibs = [1, 1]
     temp = 2
     for i in range(2, n+1):
         val = fibs[-1] + fibs[-2]
         fibs.append(val)
         temp += val
         if temp > total_lambs:
             break
     if 0 in fibs:
        fibs.remove(0)
     if sum(fibs) > total_lambs:
         del fibs[-1]
     print(fibs)
     return len(fibs)
    
def answer(total_lambs):
    total = 0
    counter = 0
    if total_lambs > 10**9 or total_lambs < 10:
        gen = [1]
    else:
        gen = []
    while counter <= total_lambs:
        current_value = 2 ** counter
        total += current_value
        if total > total_lambs:
            break
        gen.append(current_value)
        counter += 1
    print(gen)
    return fib_to(len(gen)* 3, total_lambs) - len(gen)

print(answer(10))
