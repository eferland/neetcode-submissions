class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = [[0] * 9] * 9
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if rows[i][int(board[i][j])-1] == 1 or cols[j][int(board[i][j])-1] == 1 or boxes[3*(i//3)+(j//3)][int(board[i][j])-1] == 1:
                        return False
                    rows[i][int(board[i][j])-1] += 1
                    cols[j][int(board[i][j])-1] += 1
                    boxes[3*(i//3)+(j//3)][int(board[i][j])-1] += 1
        return True