def merge(left_array, right_array):
  sorted_list = []

  left_index = 0
  right_index = 0

  while  left_index < len(left_array) and right_index < len(right_array):
    if left_array[left_index] > right_array[right_index]:
      sorted_list.append(right_array[right_index])
      right_index += 1
    else:
      sorted_list.append(left_array[left_index])
      left_index += 1
  
  while left_index < len(left_array):
    sorted_list.append(left_array[left_index])
    left_index += 1
  while right_index < len(right_array):
    sorted_list.append(right_array[right_index])
    right_index += 1
  
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
