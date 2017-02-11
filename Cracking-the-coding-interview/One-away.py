import math
def oneaway(string1, string2):
    #replace
    if len(string1) == len(string2):
        replace = False
        for x in range(0,len(string2)):
            if string1[x] != string2[x]:
                if replace:
                    return False
                else:
                    replace = True
        return True
    #char insert or delete
    if abs(len(string1)-len(string2)) == 1:
        container = {}
        for x in string1:
            if x in container:
                container[x] += 1
            else:
                container[x] = 1
        for x in string2:
            if x in container:
                container[x] -= 1
            else:
                container[x] = 1
        for key,val in container.items():
            if abs(val) > 1:
                return False
        return True
         
            
print(oneaway("pale","ple"))
print(oneaway("pales","pale"))
print(oneaway("pale","bale"))
print(oneaway("pale","bake"))
