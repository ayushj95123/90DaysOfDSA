#problem https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
class Solution:
    def findPath(self, m, n):
        # code here
        visited = [[0]*n for i in range(n)]
        visited[0][0] = 1
        curr =""
        final = []
        if m[0][0] == 0:
            return []
        self.getPaths(m,n,0,0,visited,curr, final)
        return final
    
    def getPaths(self, m,n,row,col, visited,curr, final):

        if row == n-1 and col == n-1:

            final.append(curr[:])
            return
        
        if self.isSafe(m,n,row-1,col, visited):
            visited[row-1][col] = 1
            self.getPaths(m,n, row-1,col, visited, curr+"U", final)
            visited[row-1][col] = 0
        
        if self.isSafe(m,n,row+1,col, visited):
            visited[row+1][col] = 1
            self.getPaths(m,n, row+1,col, visited, curr+"D", final)
            visited[row+1][col] = 0
        
        if self.isSafe(m,n,row,col-1, visited):
            visited[row][col-1] = 1
            self.getPaths(m,n, row,col-1, visited, curr+"L", final)
            visited[row][col-1] = 0
            
        if self.isSafe(m,n,row,col+1, visited):
            visited[row][col+1] = 1
            self.getPaths(m,n, row,col+1, visited, curr+"R", final)
            visited[row][col+1] = 0
        
    
    def isSafe(self,m,n,row,col, visited):

        return (row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1 and visited[row][col] == 0)
