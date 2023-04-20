#problem https://leetcode.com/problems/partition-equal-subset-sum/submissions/936895805/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 0:
            return self.sumDP(len(nums), int(total/2), nums)
        else:
            return False 

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