def flip_horizontal_axis(matrix):
    index1 = 0
    index2 = len(matrix)-1
    while index1 < index2:
        temp = matrix[index1]
        matrix[index1] = matrix[index2]
        matrix[index2] = temp
        index1 += 1 
        index2 -= 2 
        
        
    """
    matrix.reverse()
    
    #works just as well
    """
