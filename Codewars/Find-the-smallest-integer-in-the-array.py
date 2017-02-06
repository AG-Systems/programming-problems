def findSmallestInt(arr):
    #Code here
    counter = arr[0]
    for x in range(0,len(arr)):
        if arr[x] < counter:
            counter = arr[x]
    return counter
