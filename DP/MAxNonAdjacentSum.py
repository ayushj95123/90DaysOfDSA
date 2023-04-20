def maximumNonAdjacentSum(nums):    
    # Write your code here.
	#return maxRec(nums, len(nums))
	# dp = [-1]*len(nums)
	# return maxMemo(nums, len(nums), dp)
	return maxDP(nums)


def maxRec(n, ind):
	if ind == 1:
		return n[0]
	if ind == 2:
		return max(n[0], n[1])
	
	take = n[ind-1] + maxRec(n, ind-2)
	dont = maxRec(n, ind-1)
	return max(take, dont)

def maxMemo(n, ind, dp):
	if ind == 1:
		return n[0]
	if ind == 2:
		return max(n[0], n[1])
	
	if dp[ind-1] != -1:
		return dp[ind-1]
	
	take = n[ind-1] + maxMemo(n, ind-2, dp)
	dont = maxMemo(n, ind-1, dp)
	dp[ind-1] = max(take, dont)
	return dp[ind-1]

def maxDP(n):
	dp = [-1]*(len(n)+1)

	dp[1] = n[0]
	if len(n) == 1:
		return dp[1]
	dp[2] = max(n[0], n[1])

	for ind in range(3, len(n)+1):
		take = n[ind-1] + dp[ind-2]
		dont = dp[ind-1]
		dp[ind] = max(take, dont)
	
	return dp[len(n)]