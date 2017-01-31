def substringcounter(main,sub):
    counter = 0
    amount = 0
    for x in range(0,len(main)):
        if main[x] == sub[counter]:
            counter += 1
        else:
            counter = 0
        if counter == len(sub):
            amount += 1
            counter = 0
    print(amount)
    return amount
substringcounter("max was here", "max")
substringcounter("max and max went to the max resturant", "max")
substringcounter("I went to the park", "went to")
substringcounter("hi", "x")
