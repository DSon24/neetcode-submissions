class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range (9):
            dup = set()
            for i in range (9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in dup:
                    return False
                else:
                    dup.add(board[row][i])

        for col in range (9):
            dup = set()
            for i in range (9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in dup:
                    return False
                else:
                    dup.add(board[i][col])
        
        for square in range(9):
            dup = set()
            for i in range (3):
                for j in range (3):
                    cols = (square %3)*3 + j
                    rows = (square // 3)*3 + i

                    if board[rows][cols] == ".":
                        continue
                    elif board[rows][cols] in dup:
                        return False
                    else:
                        dup.add(board[rows][cols])
        return True


        