class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        for x in range(col):
            if obstacleGrid[0][x] != 1:
                obstacleGrid[0][x] = -1
            else:
                break
		

        for x in range(row):
            if obstacleGrid[x][0] != 1:
                obstacleGrid[x][0] = -1
            else:
                break 
        
        for y in range(1, row):
            for x in range(1, col):
                if obstacleGrid[y][x] != 1:
                    if obstacleGrid[y][x-1] != 1:
                        obstacleGrid[y][x] += obstacleGrid[y][x-1]
                    if obstacleGrid[y-1][x] != 1:
                        obstacleGrid[y][x] += obstacleGrid[y-1][x]
        
        return -1 * obstacleGrid[-1][-1]
