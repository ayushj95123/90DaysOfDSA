    def lisMemo(self, ind, prev, nums, dp):
        if ind == len(nums):
            return 0
        
        if dp[ind][prev] != -1:
            return dp[ind][prev]
    
        take = 0
        dont = 0
        if prev == -1 or nums[ind] > nums[prev]:
            take = 1 + self.lisMemo(ind+1, ind,nums, dp)

        
        dont = self.lisMemo(ind+1, prev ,nums, dp)
        dp[ind][prev] = max(take, dont)
        return dp[ind][prev]

    def lisDP(self,nums):
        dp = [[0 for j in range(len(nums)+1) ] for i in range(len(nums)+1)]

        for ind in reversed(range(len(nums))):
            for prev in range(ind-1, -2, -1):
                if ind == len(nums):
                    dp[ind][prev+1] = 0
                
                else:
                    take = 0
                    dont = 0
                    if prev == -1 or nums[ind] > nums[prev]:
                        take = 1 + dp[ind+1][ind+1]

                    
                    dont = dp[ind+1][prev+1]
                    dp[ind][prev+1] = max(take, dont)


        return dp[0][0]

    def lisNew(self, nums):
        dp = [1]*len(nums)
        maxi = float("-inf")
        for ind in range(len(nums)):
            for pre in range(ind):
                if nums[pre] < nums[ind]:
                    dp[ind] = max(dp[ind], dp[pre]+1)
            maxi = max(maxi, dp[ind])
        
        return maxi