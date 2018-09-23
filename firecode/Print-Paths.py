def print_paths( board):
    if board == [[]]:
      return []
    container = []
    def dfs(board, x, y, path):
        if y > len(board[0]) - 1 or x > len(board) - 1:
          if path not in container and path[-1] == board[-1][-1]:
            container.append(path)
          return None
        path += board[x][y]
        
        dfs(board, x + 1, y, path)
        dfs(board, x, y + 1, path)
    dfs(board, 0, 0, "")

    return container
  
board1 = [
  ['A', 'X'], 
  ['D', 'E']
]

board2 = [
  ['A', 'B', 'C']
]

board3 = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L']
]

board4 = [
  []
]
#print(len(board3))
print(print_paths(board4))
