class Solution:
    def climbStairs(self, n: int) -> int:
        #ways = self.stairRec(n)
        ways = self.stairDP(n)
        return ways

    
    def stairRec(self, n):
        if n ==1 or n ==2:
            return n
    
        return self.stairRec(n-1) + self.stairRec(n-2)

    
    def stairDP(self, n):
         
        dp = [1] * (n+1)

        for stair in range(n+1):
            if stair < 3:
                dp[stair] = stair
            else:
                dp[stair] = dp[stair-1] + dp[stair-2]
        print(dp)
        
        return dp[n]