class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for row in range(0, n):
            row = [0] * m
            grid.append(row)
        
        def unique_paths(grid, row, col):
            if row > len(grid[0]) - 1 or col > len(grid) - 1:
                return 0
            if row == len(grid[0]) - 1 and col == len(grid) - 1:
                return 1
            return unique_paths(grid, row + 1, col) + unique_paths(grid, row, col + 1)
        
        if grid != []:
            return unique_paths(grid, 0, 0)
        else:
            return 0
