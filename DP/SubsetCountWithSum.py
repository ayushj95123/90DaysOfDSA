#https://www.codingninjas.com/codestudio/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1
def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
	#result = findWay(num, tar, len(num)-1)
	# n = len(num)
	# dp = [[-1 for j in range(tar+1)] for i in range(n)]
	# result = findWayMemo(num, tar, n-1, dp)
	# return result

	return findWayDP(num, tar)


def findWay(nums, tar, ind):	
	if tar == 0:
		return 1
	if ind == 0:
		return 1 if nums[0] == tar else 0
	
	take = findWay(nums, tar-nums[ind], ind-1)
	dontTake = findWay(nums, tar, ind-1)

	return take + dontTake

def findWayMemo(nums, tar, ind, dp):	
	if tar == 0:
		return 1
	if ind == 0:
		return 1 if nums[0] == tar else 0
	if tar < 0:
		return 0
	
	if dp[ind][tar] != -1:
		return dp[ind][tar]
	
	
	
	take = findWayMemo(nums, tar-nums[ind], ind-1, dp)
	dontTake = findWayMemo(nums, tar, ind-1, dp)

	dp[ind][tar] = take + dontTake
	return dp[ind][tar]


def findWayDP(nums, tar):	
	dp = [[-1 for j in range(tar+1)] for i in range(len(nums))]
	for ind in range(len(nums)):
		for tar in range(tar+1):
			if tar == 0:
				dp[ind][tar] = 1
			elif ind == 0:
				dp[ind][tar] = 1 if nums[0] == tar else 0
			else:
				take = dp[ind-1][tar-nums[ind]] if tar-nums[ind] >= 0 else 0
				dontTake = dp[ind-1][tar]
				dp[ind][tar] = take + dontTake
	
	return dp[len(nums)-1][tar]