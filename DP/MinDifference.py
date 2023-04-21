class Solution:
    def minimumDifference(self, nums) :
        print("Called")

        total = sum(nums)

        mini = float("inf")

        for i in range(1, total):
            if self.sumDP(len(nums), i, nums):

                diff = abs(i - (total - i))
                print("Succesful for ", i, " diff:", diff )
                mini = min(mini, diff)
                print("Mini:", mini)

        print("Final: ", mini)
        return mini

    def sumDP(self, n, tar, arr):
        dp = [[False for j in range(tar+1)] for i in range(n)]
	
        for ind in range(n):
            for k in range(tar+1):
                if k == 0:
                    dp[ind][k] = True
                elif ind == 0:
                    dp[ind][k] = (k == arr[0])
			
                else:
                    take = dp[ind-1][k-arr[ind]] if k-arr[ind] >= 0 else False
                    dontTake = dp[ind-1][k]
                    dp[ind][k] = take or dontTake
        return dp[n-1][tar]
    

sol = Solution()
ans = sol.minimumDifference([3,9,7,3])
print(ans)