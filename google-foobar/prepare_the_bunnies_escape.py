def paths(grid):
    m = len(grid)
    n = len(grid[0])
    ways = [[0 for _ in range(m)] for _ in range(n)]
    if grid[0][0] == 1:
        return 0
    ways[0][0] = 1
    for x in range(1,m):
        if grid[x][0] != 1:
            ways[x][0] = ways[x-1][0]
    print(ways)
    for x in range(1,n):
        if grid[0][x] != 1:
            ways[0][x] = ways[0][x-1]
    print(ways)
    for x in range(1,m):
        for z in range(1,n):
            if grid[x][z] != 1:
                ways[x][z] = ways[x][z-1] + ways[x-1][z]
    print(ways)
    return ways[m-1][n-1]

print(paths([[0,0,0],[0,1,0],[0,0,0]]))
