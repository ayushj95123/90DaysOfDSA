#Problrm https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.getSudokuArrangement(board)
    
    def getSudokuArrangement(self, board, row=0, col=0):
        if row == 9:
            return True
        if board[row][col] == ".":
            for num in range(1,10):
                if self.isSafe(board, row, col, str(num)):
                    board[row][col] = str(num)
                    newcol = col
                    newrow = row
                    if col == 8:
                        newcol = 0
                        newrow = row+1
                    else:
                        newcol = col+1
                    
                    if self.getSudokuArrangement(board, newrow, newcol):
                        return True
                    board[row][col] = "."
            return False
        else:
            if col == 8:
                col = 0
                row = row+1
            else:
                col = col+1
            return self.getSudokuArrangement(board, row, col)