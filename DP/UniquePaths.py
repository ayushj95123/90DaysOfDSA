def uniquePaths(m, n):
	# Write your code here.
    if m==1 and n==1:
        return 1
    #return uniquePathUtil(m-1,n-1)
    #return uniqueDP(m,n)
    return uniqueDPOptimized(m,n)
    pass

def uniquePathUtil(row, col):    
    if row == 0  or col == 0:
        return 1
    else:
        upWays = uniquePathUtil(row-1, col)
        leftWays = uniquePathUtil(row, col-1)
        return upWays + leftWays
    
    
def uniqueDP(rows, cols):
    dp = [[0 for i in  range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[rows-1][cols-1]

def uniqueDPOptimized(rows, cols):
    prev = [1 for i in  range(cols)]
    curr = [0 for i in  range(cols)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                curr[col] = 1
            else:
                curr[col] = prev[col] + curr[col-1]
        prev = curr[:]
    return prev[cols-1]