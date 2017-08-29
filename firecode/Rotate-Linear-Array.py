def rotate_left(list_numbers,k):
    l = []
    if k < len(list_numbers):
        l.extend(list_numbers[k:len(list_numbers)])
        l.extend(list_numbers[0:k])
    else:
        while k > len(list_numbers):
            k = k - len(list_numbers)
        l.extend(list_numbers[k:len(list_numbers)])
        l.extend(list_numbers[0:k])        
    return l
