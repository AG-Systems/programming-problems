class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [] or board == None:
            if word == "" or word == None:
                return True
            else:
                return False
        
        def get_position(grid, row, col, letter):
            for y in range(row, len(grid)):
                for x in range(col, len(grid[y])):
                    if letter == grid[y][x]:
                        return [y,x]
            return [-1,-1]
        def is_valid_move(grid, row, col):
            if row > len(grid) - 1 or col > len(grid[0]) - 1:
                return False
            else:
                return True
        def string_builder(grid, row, col, paths, word, index):
            if not is_valid_move(grid, row, col):
                return 0
            if grid[row][col] != word[index]:
                return 0
            if grid[row][col] == word[index] and index == len(word):
                return 1
            
            if paths[row][col] == 0:
                paths[row][col] = 1
                index += 1
                down = string_builder(grid, row + 1, col, paths, word, index)
                right = string_builder(grid, row, col + 1, paths, word, index)
                up = string_builder(grid, row - 1, col, paths, word, index)
                left = string_builder(grid, row, col - 1, paths, word, index)
                return sum([down, right, up, left])
            else:
                return 0
        starting_pos = get_position(board, 0, 0, word[0]) # [y,x]
        starting_paths = [ [0] * len(board[0]) ] * len(board)
        
        while is_valid_move(board, starting_pos[0], starting_pos[1]):
            paths = list(starting_paths)
            if string_builder(board, starting_pos[0], starting_pos[1], paths, word, 0) >= 1:
                return True
            else:
                starting_pos = get_position(board, starting_pos[0], starting_pos[1] + 1, word[0])
        return False
        
