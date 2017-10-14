def namelist(names):
    #your code here

    total_names = ""
    counter = 0
    for x in names:
        counter += 1
        if counter == (len(names)-1):
            total_names += str(x["name"] + " & ")
        elif counter == len(names):
            total_names += str(x["name"])
        else:
            total_names += str(x["name"] + ", ")
    return total_names
