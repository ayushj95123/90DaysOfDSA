#problem https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=0&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
def subsetSumToK(n, k, arr):

    #return sumRec(n,k, arr, len(arr)-1)

	# dp = [[-1 for j in range(k+1)] for i in range(n)]

	# return sumMemo(n,k,arr, len(arr)-1, dp)

	return sumDP(n, k, arr)

	


def sumRec(n, k, arr, ind):
	if k == 0:
		return True
	
	if ind < 0 or k < 0:
		return False
	
	take = sumRec(n, k-arr[ind], arr, ind-1)
	dontTake = sumRec(n, k, arr, ind-1)

	return take or dontTake

def sumMemo(n, k, arr, ind, dp):
	if k == 0:
		return True
	
	if ind < 0 or k < 0:
		return False
	
	if dp[ind][k] != -1:
		return dp[ind][k] 
	
	take = sumMemo(n, k-arr[ind], arr, ind-1, dp)
	dontTake = sumMemo(n, k, arr, ind-1, dp)

	dp[ind][k] = take or dontTake
	return dp[ind][k]

def sumDP(n, tar, arr):
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