def transpose_matrix(matrix):
    import copy
    copy_m = copy.deepcopy(matrix)
    for x in xrange(len(matrix)):
        for z in xrange(len(matrix[x])):
            matrix[x][z] = copy_m[z][x]
