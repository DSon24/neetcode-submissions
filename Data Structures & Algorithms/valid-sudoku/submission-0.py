class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range (9):
            rset = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                elif board[row][j] in rset:
                    return False
                else:
                    rset.add(board[row][j])

        for col in range (9):
            cset = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                elif board[j][col] in cset:
                    return False
                else:
                    cset.add(board[j][col])
        
        for square in range(9):
            sset = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3)*3 + i
                    col = (square % 3)*3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in sset:
                        return False
                    else:
                        sset.add(board[row][col])
        return True
                

        