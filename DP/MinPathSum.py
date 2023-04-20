#problem https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1
def minSumPath(grid):
    # Write your code here.
	n = len(grid)
	m = len(grid[0])
	#return sumRec(grid, n, m, n-1, m-1 )
	# dp = [[-1 for col in range(m)] for row in range(n)]
	# return sumMemo(grid, n, m, n-1, m-1, dp)\
	
	return sumDP(grid, n, m)

def sumRec(grid, n, m, row, col):
	if row == 0 and col ==0:
		return grid[0][0]
	
	left = float("inf")
	up = float("inf")
	
	if col - 1 >= 0:
		left = grid[row][col] + sumRec(grid, n, m, row, col-1) 
	if row - 1 >= 0:
		up = grid[row][col] + sumRec(grid, n, m, row-1, col)

	return min(left, up) 

def sumMemo(grid, n, m, row, col, dp):
	if row == 0 and col ==0:
		return grid[0][0]

	if dp[row][col] != -1:
		return dp[row][col]
	
	left = float("inf")
	up = float("inf")
	
	if col - 1 >= 0:
		left = grid[row][col] + sumRec(grid, n, m, row, col-1) 
	if row - 1 >= 0:
		up = grid[row][col] + sumRec(grid, n, m, row-1, col)

	dp[row][col] =  min(left, up) 
	return dp[row][col]

def sumDP(grid, n, m):
	dp = [[-1 for col in range(m)] for row in range(n)]

	for row in range(n):
		for col in range(m):
			
			if row == 0 and col ==0:
				dp[0][0] = grid[0][0] 
			else:
				left = float("inf")
				up = float("inf")
	
				if col - 1 >= 0:
					left = grid[row][col] + dp[row][col-1] 
				if row - 1 >= 0:
					up = grid[row][col] + dp[row-1][col]

				dp[row][col] =  min(left, up) 
				
	return dp[n-1][m-1]