#problem https://leetcode.com/problems/triangle/description/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #return self.minRec(triangle, 0, 0)

        # dp = []
        # for row in triangle:
        #     dp.append([-1]*len(row))
        # return self.minMemo(triangle, 0,0,dp)

        return self.minDPOptimized(triangle)

    
    def minRec(self, t, row, col):
        if row == len(t)-1:
            return t[row][col]

        down = t[row][col] + self.minRec(t, row+1, col)
        

        adj = t[row][col] + self.minRec(t, row+1, col+1)
        
        return min(down, adj)

    def minMemo(self, t, row, col, dp):
        if row == len(t)-1:
            return t[row][col]
        
        if dp[row][col] != -1:
            return dp[row][col]

        down = t[row][col] + self.minMemo(t, row+1, col, dp)
        

        adj = t[row][col] + self.minMemo(t, row+1, col+1, dp)
        
        dp[row][col] = min(down, adj)
        return dp[row][col]

    def minDP(self, t):
        dp = []
        for row in t:
            dp.append([-1]*len(row))

        
        for row in reversed(range(len(dp))):
            for col in reversed(range(len(t[row]))):
                if row == len(t)-1:
                    dp[row][col] = t[row][col]
                else:
                    down = t[row][col] + dp[row+1][col]
                    adj = t[row][col] + dp[row+1][col+1]
                    dp[row][col] = min(down, adj)
        return dp[0][0]

    def minDPOptimized(self, t):        

        
        for row in reversed(range(len(t))):
            curr = [-1]* len(t[row])
            for col in reversed(range(len(t[row]))):
                if row == len(t)-1:
                    curr[col] = t[row][col]
                else:
                    down = t[row][col] + nxt[col]
                    adj = t[row][col] + nxt[col+1]
                    curr[col] = min(down, adj)
            nxt = curr[:]
        return nxt[0]