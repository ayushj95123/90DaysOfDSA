def unboundedKnapsack(n, w, profit, weight):
    
    return knapSack(w, weight, profit)

def knapSack(W,w,v):
	dp = [[0 for j in range(W+1)] for i in range(len(v)+1)]
	
	for ind in range(1,len(v)+1):
		for wt in range(1, W+1):
			
			take = dp[ind][wt-w[ind-1]] + v[ind-1] if wt-w[ind-1] >= 0 else 0
			dontTake = dp[ind-1][wt] 
			
			dp[ind][wt] = max(take, dontTake)
	
	return dp[len(v)][W]