def merge(left_array, right_array):
  sorted_list = []

  while len(left_array) > 0 and len(right_array) > 0:
    if left_array[0] > right_array[0]:
      sorted_list.append(right_array[0])
      right_array.pop(0)
    else:
      sorted_list.append(left_array[0])
      left_array.pop(0)
  

  while len(left_array) > 0:
    sorted_list.append(left_array[0])
    left_array.pop(0)
  while len(right_array) > 0:
    sorted_list.append(right_array[0])
    right_array.pop(0)
  
  return sorted_list

def merge_sort(array):
  if len(array) == 1:
    return array

  length = len(array) // 2
  left_array = array[0:length]
  right_array = array[length: len(array)] 
  left_array = merge_sort(left_array)
  right_array = merge_sort(right_array)

  return merge(left_array,right_array)


print(merge_sort([2,5,1,3,7,8,9]))
