def factors(n):   
    import functools
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
                
def list_squared(m, n):
    import math
    results = []
    for i in range(m,n):
        listnums = sorted(factors(i))
        listnums = sum(map(lambda x: x * x, listnums))
        final_num = math.sqrt( listnums )
        if final_num.is_integer():
            results.append([i, listnums])
    return results
    
"""
def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret

I LIKE THIS SOLUTION


"""
