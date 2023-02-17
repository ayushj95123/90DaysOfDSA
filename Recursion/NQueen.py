#problem https://leetcode.com/problems/n-queens/submissions/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        final = []
        curr = [["."]*n for i in range(n)]
        self.getQueenPlacements(n, 0, curr, final)
        return final
    



    def getQueenPlacements(self, n,row, curr, final):
        if row == n:
            arrangement = ["".join(row) for row in curr]
            final.append(arrangement)
            return
        
        for col in range(n):
            if self.isSafe(curr, row, col):
                curr[row][col] = "Q"
                self.getQueenPlacements(n, row+1, curr, final)
                curr[row][col] = "."

    
    def isSafe(self, a, row, col):
        #check up
        for i in range(0, row):
            if a[i][col] == "Q":
                return False
        
        #Check diagonal left
        i = row-1
        j = col-1
        while i >= 0 and j>=0:
            if a[i][j] == "Q":
                return False
            i = i-1
            j = j-1
        
        #check diagonal right
        i = row-1
        j = col+1
        while i>= 0 and j<len(a[0]):
            if a[i][j] == "Q":
                return False
            i = i-1
            j = j+1
        
        return True