class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range (9):
            hash_row = set()
            for i in range(9):
                if board[row][i] in hash_row:
                    return False
                elif board[row][i] == ".":
                    continue
                else:
                    hash_row.add(board[row][i])
        
        for col in range(9):
            hash_col = set()
            for i in range (9):
                if board[i][col] in hash_col:
                    return False
                elif board[i][col] == ".":
                    continue
                else:
                    hash_col.add(board[i][col])
        
        for square in range(9):
            hash_sq = set()
            for row in range(3):
                for col in range(3):
                    r = (square // 3) *3 + row
                    c = (square % 3)*3 + col
                    if board[r][c] in hash_sq:
                        return False
                    elif board[r][c] == ".":
                        continue
                    else:
                        hash_sq.add(board[r][c])
        return True
