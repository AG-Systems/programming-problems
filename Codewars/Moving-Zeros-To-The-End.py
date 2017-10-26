def move_zeros(array):
    #your code here
    num_list = []
    z_list = []
    for x in range(len(array)):
        if array[x] != 0:
            num_list.append(array[x])
        else:
            z_list.append(0)
    array = num_list + z_list
    return array
