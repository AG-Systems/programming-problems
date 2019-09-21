def next_smaller(n):
    if len(str(n)) <= 1:
        return -1
    list_num = [int(x) for x in str(n)]
    if sorted(list_num) == list_num:
        return -1

    
    
    
    
