def max_gain(input_list):
    min_num = min(input_list)
    max_num = max(input_list)
    if input_list.index(min_num) < input_list.index(max_num):
        return max_num - min_num
    else:
        return 0
