class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        
        
        def dfs(grid, y, x):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) or grid[y][x] == "0":
                return 0
            
            grid[y][x] = "0"
            dfs(grid, y + 1, x)
            dfs(grid, y - 1, x)
            dfs(grid, y, x + 1)
            dfs(grid, y, x - 1)
            return 1
            
            
        num_of_islands = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == "1":
                    num_of_islands += dfs(grid, y, x)
        
        return num_of_islands
