def sort_array(source_array):
    # Return a sorted array.
    if source_array == []:
        return []
    odd_list = []
    for x in source_array:
        if not x % 2 == 0:
            odd_list.append(x)
    odd_list.sort()
    counter = 0
    for x in range(len(source_array)):
        val = source_array[x]
        if not val % 2 == 0:
            source[x] = odd_list[counter]
            counter += 1
    return source_array
