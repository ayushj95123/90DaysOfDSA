#problem https://www.codingninjas.com/codestudio/problems/maze-obstacles_977241?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1
def mazeObstacles(n, m, mat):
    return mazeDP(n,m, mat)
    # Write your code here.

def mazeRec(n,m, mat, row, col):
    if row == 0 and col == 0:
        return 1
    
    if mat[row][col] == -1:
        return 0
    
    up = mazeRec(n,m, mat, row-1, col) if row-1 >= 0 else 0
    left = mazeRec(n,m, mat, row, col-1) if col-1 >=0 else 0

    return (up + left) % modulo

def mazeDP(n,m,mat):
    dp = [[0 for col in range(m)] for row in range(n)]
    
    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0:
                dp[row][col] = 1
            elif mat[row][col] == -1:
                dp[row][col] = 0
            else:
                up = dp[row-1][col] if row-1 >= 0 else 0
                left = dp[row][col-1] if col-1 >=0 else 0
                dp[row][col] = (up + left) % modulo
    return dp[n-1][m-1]