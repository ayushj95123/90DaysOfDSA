#Problem https://www.codingninjas.com/codestudio/problems/house-robber_839733?leftPanelTab=1
def houseRobber(valueInHouse):
    # Write your function here.
    if len(valueInHouse) == 1:
        return valueInHouse[0]
    exceptFirst = robberDP(valueInHouse[1:])
    exceptLast = robberDP(valueInHouse[:-1])
    return max(exceptFirst, exceptLast)


def robberRec(v, ind):
    if ind == 1:
        return v[0]
    if ind == 2:
        return max(v[0], v[1])
    
    take = v[ind-1] + robberRec(v, ind-2)
    dontTake = robberRec(v, ind-1)
    return max(take, dontTake)

def robberDP(v):
    dp = [-1]*(len(v)+1)
    dp[1] = v[0]
    dp[2] = max(v[0], v[1])
    
    for ind in range(3, len(v)+1):
        take = v[ind-1] + dp[ind-2]
        dontTake = dp[ind-1]
        dp[ind] = max(take, dontTake)
    
    return dp[len(v)]