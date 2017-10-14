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


"""
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
#WOW CLEVER SOLUTION
"""        
