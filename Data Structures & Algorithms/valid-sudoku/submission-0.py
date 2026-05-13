class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num not in seen:
                    seen.add(num)
                else:
                    return False

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for row in range(box_row,box_row+3):
                    
                    for col in range(box_col,box_col+3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] not in seen:
                            seen.add(board[row][col])
                        else:
                            return False
        return True
