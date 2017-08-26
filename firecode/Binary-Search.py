def binary_search(a_list, item):
    while len(a_list) > 0:
        mid = len(a_list) / 2
        if item == a_list[mid]:
            return True
        else:
            if item < a_list[mid]:
                a_list = a_list[0:mid]
            else:
                a_list = a_list[mid:-1]
    return False
