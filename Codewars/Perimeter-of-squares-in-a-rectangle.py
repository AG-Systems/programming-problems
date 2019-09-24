def perimeter(n):
    squares = [None] * (n + 1)
    squares[0] = 1
    squares[1] = 1
    
    for index in range(2, n + 1):
        squares[index] = squares[index - 1] + squares[index - 2]
    
    return 4 * (sum(squares))
