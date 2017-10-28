def move_zeros(array):
    #your code here
    if array.count(False) > 0:
        num_list = []
        z_list = []
        
        for x in range(len(array)):
            if array[x] == 0 or array[x] == 0.0:
                if type(array[x]) == int or type(array[x]) == float:
                    z_list.append(0)
                else:
                    num_list.append(array[x])
            else:
                num_list.append(array[x])

        array = num_list + z_list
        return array
    else:
        counter = array.count(0)
        array = filter(lambda a: a != 0, array)
        lk = [0] * counter
        array = array + lk
        return array
