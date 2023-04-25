def getMaximumProfit(values, n) :
	#Your code goes here
    #return maxRec(0, True, values, n)
    # dp = [[-1 for j in range(2)] for i in range(n)]
    # return maxMemo(0, 1, values, n, dp)
    return maxDP(values, n)


def maxRec(ind, canBuy, v, n):
    if ind >= len(v):
        return 0

    if canBuy:
        return max(maxRec(ind+1, False, v, n) - v[ind], maxRec(ind+1, True, v, n))
    else:
        return max(maxRec(ind+1, True, v, n) + v[ind], maxRec(ind+1, False, v,n))

def maxMemo(ind, canBuy, v, n, dp):
    if ind >= len(v):
        return 0
    
    if dp[ind][canBuy] != -1:
        return dp[ind][canBuy]

    if canBuy:
        dp[ind][canBuy] = max(maxMemo(ind+1, 0, v, n, dp) - v[ind], maxMemo(ind+1, 1, v, n, dp))
    else:
        dp[ind][canBuy] = max(maxMemo(ind+1, 1, v, n, dp) + v[ind], maxMemo(ind+1, 0, v,n, dp))
        
    return dp[ind][canBuy]


def maxDP(v, n):

    dp = [[-1 for j in range(2)] for i in range(n+1)]

    for ind in reversed(range(n+1)):
        for canBuy in range(2):
            if ind >= n:
                dp[ind][canBuy] = 0
            else:

                if canBuy:
                    dp[ind][canBuy] = max(maxMemo(ind+1, 0, v, n, dp) - v[ind], maxMemo(ind+1, 1, v, n, dp))
                else:
                    dp[ind][canBuy] = max(maxMemo(ind+1, 1, v, n, dp) + v[ind], maxMemo(ind+1, 0, v,n, dp))
        
    return dp[0][1]