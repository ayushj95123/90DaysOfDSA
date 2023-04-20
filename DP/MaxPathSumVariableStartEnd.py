#problem https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0
def getMaxPathSum(matrix):

    return maxDP(matrix)

def maxDP(t):
    dp = []
    for row in t:
        dp.append([-1]*len(row))

        
    for row in reversed(range(len(dp))):
        for col in reversed(range(len(t[row]))):
            if row == len(t)-1:
                dp[row][col] = t[row][col]
            else:
                down = t[row][col] + dp[row+1][col]
                adjRight = t[row][col] + dp[row+1][col+1] if col != len(t[row])-1 else float("-inf")
                adjLeft = t[row][col] + dp[row+1][col-1] if col != 0 else float("-inf")
                dp[row][col] = max([down, adjRight, adjLeft])
    return max(dp[0])