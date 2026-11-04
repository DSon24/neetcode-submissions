class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range (9):
            set_row = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in set_row:
                    return False
                else:
                    set_row.add(board[row][i])
        

        for col in range(9):
            set_col = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in set_col:
                    return False
                else:
                    set_col.add(board[i][col])
        
        for square in range(9):
            square_set = set()
            for row in range(3):
                for col in range(3):
                    r = (square // 3)*3 + row
                    c = (square % 3)*3 + col

                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in square_set:
                        return False
                    else:
                        square_set.add(board[r][c])
        return True
                
        