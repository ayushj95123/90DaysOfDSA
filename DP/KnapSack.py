
def knapSack(ind, W, w, v):
	if W == 0:
		return 0
	if ind < 0:
		return 0
	

	take = knapSack(ind-1, W-w[ind], w,v) + v[ind] if W-w[ind] >=0 else 0
	
	dont = knapSack(ind-1, W, w,v)

	return max(take, dont)

def knapSackMemo(ind, W, w, v, dp):
	if W == 0:
		return 0
	if ind < 0:
		return 0
	
	if dp[ind][W] != -1:
		return dp[ind][W]

	take = knapSackMemo(ind-1, W-w[ind], w,v, dp) + v[ind] if W-w[ind] >=0 else 0
	
	dont = knapSackMemo(ind-1, W, w,v, dp)

	dp[ind][W] = max(take, dont)
	return dp[ind][W] 


def knapSackDP(n, W, w, v):
	dp = dp = [[ 0 for j in range(W+1)] for i in range(n+1)]

	for ind in range(1, n+1):
		for wt in range (1, W+1):
			take = dp[ind-1][wt-w[ind-1]]+ v[ind-1] if wt-w[ind-1] >=0 else 0
			dont = dp[ind-1][wt]
			dp[ind][wt] = max(take, dont)
	return dp[n][W] 


def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		w = [int(x) for x in input().split()]
		v = [int(x) for x in input().split()]
		W = int(input())
		dp = [[ -1 for j in range(W+1)] for i in range(n+1)]
		print(knapSackDP(n, W, w, v))

if __name__ == "__main__":
	main()