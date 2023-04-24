def countWaysToMakeChange(denominations, value) :
    
	# Your code goes here
    return minDP(value, denominations)
def minDP(tar, n):
    dp = [[ 0 for t in range(tar+1)]for ind in range(len(n))]

    for ind in range(len(n)):
        for t in range(tar+1):
            if ind == 0:
                if t == 0:
                    dp[ind][t] = 1
                else:
                    if t%n[0]:
                        dp[ind][t] = 0
                    else:
                        dp[ind][t] = 1
            else:
                take = dp[ind][t-n[ind]] if t-n[ind] >= 0 else 0
                dontTake = dp[ind-1][t]
                dp[ind][t] = take+dontTake 
    return dp[len(n)-1][tar]