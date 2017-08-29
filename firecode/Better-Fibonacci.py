def helper(n, container):
    if n <= 1:
        return n
    else:
        if container[n-1] == 0:
            container[n-1] = helper(n-1, container)
        if container[n-2] == 0:
            container[n-2] = helper(n-2, container)
        container[n] = container[n-1] + container[n-2]
    return container[n]

        

def better_fibonacci(n):
    l = [0 for _ in range(n+1)]
    return helper(n,l)

"""
def better_fibonacci(n):
    n2 = 0
    n1 = 1
    if n == 0:
        return n2
    elif n == 1:
        return n1
    counter = 2
    while counter <= n:
        temp = n1 + n2
        n2 = n1
        n1 = temp
        counter += 1
    return n1
    
Better solution 
"""
