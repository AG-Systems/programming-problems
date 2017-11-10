def make_readable(seconds):
    # Do something
    counter = 0
    hours = 0
    while(seconds > 59):
        seconds -= 60
        counter += 1
    if counter > 59:
        while(counter > 59):
            hours += 1
            counter -= 60
    res = [hours,counter,seconds]
    time = ""
    for x in range(len(res)):
        if x != len(res)-1:
            if len(str(res[x])) == 1:
                time += "0" + str(res[x]) + ":"
            else:
                time += str(res[x]) + ":"
        else:
            if len(str(res[x])) == 1:
                time += "0" + str(res[x])
            else:
                time += str(res[x])
    return time
