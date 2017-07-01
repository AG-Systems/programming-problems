def get_sum(a,b):
    if a == b:
        return a
    else:
        total = 0
        min_num = min(a,b)
        max_num = max(a,b)
        for x in range(min_num, max_num + 1):
            total += x
        return total
