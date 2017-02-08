def switch(array1, array2):
    if len(array1) == len(array2):
        for x in range(0,len(array1)):
            temp = array1[x]
            array1[x] = array2[x]
            array2[x] = temp
    else:
        print("ERROR")
    print(array1, array2)

a1 = [1,2,3,4,5,6,7,8]
a2 = [123,523,7,211,1,2,3,4]
switch(a1,a2)
        
