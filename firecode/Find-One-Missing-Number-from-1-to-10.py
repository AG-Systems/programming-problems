def find_missing_number(list_numbers):
    l = [1,2,3,4,5,6,7,8,9,10]
    for x in range(len(l)):
        if l[x] != list_numbers[x]:
            return l[x]
