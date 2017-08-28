def find_partitions(input_list):
    counter = input_list[0]
    l = []
    numbered = []
    for x in input_list:
        if counter == x:
            numbered.append(x)
            counter += 1
        else:
            if len(numbered) >= 2:
                if numbered[0] == numbered[1]-1:
                    l.append(str(numbered[0]) + "-" + str(numbered[-1]))
                else:
                    if numbered[0] not in l:
                        l.append(numbered[0])
                    if numbered[1] not in l:
                        l.append(numbered[-1])
            else:
                if len(numbered) != 0:
                    l.append(numbered[0])
                l.append(x)
            numbered = [x]
            if x != input_list[-1]:
                counter = input_list[input_list.index(x)+1]
    if len(numbered) < 2:
        if len(numbered) == 1:
            l.append(numbered[0])
        return l
    else:
        if numbered[0]+1 == numbered[1]:
            l.append(str(numbered[0]) + "-" + str(numbered[-1]))
        else:
            l.append(numbered[-1])
        return l



#print(find_partitions([1,2,3,6,7,8,10,11]))
#print(find_partitions([1,3,5,7]))
#print(find_partitions([1, 3, 5]))
#print(find_partitions([1,2,5,8,10]))
#print(find_partitions([1, 3, 5, 7]))
