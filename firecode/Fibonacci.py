def helper(n, table):
    if n <= 1:
        return n
    else:
        if table[n-1] == 0:
            table[n-1] = helper(n-1,table)
        if table[n-2] == 0:
            table[n-2] = helper(n-2, table)
        table[n] = table[n-1] + table[n-2]
        return table[n]
        
def fib(n):
    l = [0 for _ in range(n+1)]
    results = helper(n, l)
    return results
    
    
