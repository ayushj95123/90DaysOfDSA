def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
	#mini = jumpRec(n, heights)
	
	mini = jumpDP(n, heights)
	return mini


def jumpRec(n, h):
	#Base Case
	if n == 2:
		return abs(h[1] - h[0])
	if n == 1:
		return 0

	single = jumpRec(n-1, h) + abs(h[n-1] - h[n-2])
	double = jumpRec(n-2, h) + abs(h[n-1] - h[n-3])
	return min(single, double)

def jumpMemo(n, h, dp):
	if n == 2:
		return abs(h[1] - h[0])
	if n == 1:
		return 0
	
	if dp[n] != -1:
		return dp[n]
	
	single = jumpMemo(n-1, h, dp) + abs(h[n-1] - h[n-2])
	double = jumpMemo(n-2, h, dp) + abs(h[n-1] - h[n-3])
	dp[n] = min(single, double)
	return dp[n]

def jumpDP(n,h):
	dp = [-1]*(n+1)


	for i in range(1, n+1):
		if i == 2:
			dp[2] = abs(h[1] - h[0])
		elif i == 1:
			dp[1] = 0
		else:
			single = dp[i-1] + abs(h[i-1] - h[i-2])
			double = dp[i-2] + abs(h[i-1] - h[i-3])
			dp[i] = min(single, double)
		
	return dp[n]