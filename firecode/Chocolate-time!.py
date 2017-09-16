def distributeChocolate(points):
    l = [1] * len(points)
    if len(l) < 1:
        return 0
    for x in range(+1, len(points)-1):
        print(l)
        if points[x-1] < points[x]:
            l[x] += 1
            if l[x] <= l[x-1]:
                l[x] = (l[x-1] + 1)
        if points[x] > points[x-1] and l[x] < l[x+1]:
            l[x] += 1
        if points[x] > points[x+1]:
            l[x] += 1
    counter = 0
    for x in xrange(max(l), 0, -1):
        if x not in l:
            counter += 1 
    return sum(l) - counter
#print(distributeChocolate([1,5,7,1])) #7
#print(distributeChocolate([2, 3, 3, 2, 1, 5, 2])) #12
#print(distributeChocolate([2])) #1
#print(distributeChocolate([])) #0

"""
    if len(points) == 0:
        return 0
    numChocolates = [1]
    for i in range(1,len(points)):
        if points[i]>points[i-1]:
            numChocolates.append(numChocolates[i-1]+1)
        else:
            numChocolates.append(1)
    result = numChocolates[len(points)-1]
    for i in range(len(points)-2,-1,-1):
        if points[i]>points[i+1]:
            numChocolates[i] = max (numChocolates[i], numChocolates[i+1]+1)
        result += numChocolates[i]
    return result
#correct solution
"""
