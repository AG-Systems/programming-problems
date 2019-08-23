def hourglassSum(arr):
    hourglass_sum_list = []


    for y in range(0, len(arr) - 2):
        for x in range(0, len(arr[0]) - 2):
            top_row = sum([ arr[y][x], arr[y][x + 1], arr[y][x + 2]])
            mid_point = arr[y + 1][x + 1]
            bottom_row = sum([ arr[y + 2][x], arr[y + 2][x + 1], arr[y + 2][x + 2]])
            sum_val = top_row + mid_point + bottom_row
            hourglass_sum_list.append(sum_val)
    
    return max(hourglass_sum_list)
