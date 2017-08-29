def rotate_square_image_ccw(matrix):
    transpose_matrix(matrix)
    flip_horizontal_axis(matrix)
    
def transpose_matrix(matrix):
    import copy
    copy_m = copy.deepcopy(matrix)
    for x in xrange(len(matrix)):
        for z in xrange(len(matrix[x])):
            matrix[x][z] = copy_m[z][x]
            

def flip_horizontal_axis(matrix):
    index1 = 0
    index2 = len(matrix)-1
    while index1 < index2:
        temp = matrix[index1]
        matrix[index1] = matrix[index2]
        matrix[index2] = temp
        index1 += 1 
        index2 -= 2 
