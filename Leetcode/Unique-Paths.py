class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for row in range(0, n):
            row = [0] * m
            grid.append(row)
        
        def unique_paths(grid, row, col, paths):
            if col > len(grid[0]) - 1 or row > len(grid) - 1:
                return 0
            if col == len(grid[0]) - 1 and row == len(grid) - 1:
                return 1
            if paths[row][col] == 0:
                paths[row][col] = unique_paths(grid, row + 1, col, paths) + unique_paths(grid, row, col + 1, paths)
            return paths[row][col]
        
        if grid != []:
            paths = list(grid)
            return unique_paths(grid, 0, 0, paths)
        else:
            return 0
