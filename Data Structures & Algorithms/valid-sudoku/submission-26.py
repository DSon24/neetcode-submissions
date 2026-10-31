class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rset = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in rset:
                    return False
                else:
                    rset.add(board[row][i])
            

        for col in range(9):
            cset = set()
            for i in range (9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in cset:
                    return False
                else:
                    cset.add(board[i][col])
        

        for square in range(9):
            squareset = set()
            for row in range(3):
                for col in range (3):
                    r = (square // 3)*3 + row
                    c = (square % 3)*3 + col

                    if board[r][c] == ".":
                        continue
                    elif board[r][c] in squareset:
                        return False
                    else:
                        squareset.add(board[r][c])
        return True