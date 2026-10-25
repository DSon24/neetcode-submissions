class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in row_set:
                    return False
                else:
                    row_set.add(board[row][i])
        
        for col in range(9):
            col_set = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in col_set:
                    return False
                else:
                    col_set.add(board[i][col])
        

        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square //3 )*3 + i
                    col = (square % 3)*3 + j

                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in square_set:
                        return False
                    else:
                        square_set.add(board[row][col])
        return True