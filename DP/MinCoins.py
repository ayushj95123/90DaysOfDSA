def minimumElements(num: List[int], x: int) -> int:
    # Write your code here.
    #dp = [[ float("inf") for tar in range(x+1)]for ind in range(len(num))]
    mini = minDP(x, num)
    if mini == float("inf"):
        return -1
    else:
        return mini


def minRec(ind, t, n):
    if ind == 0:
        if t == 0:
            return 0
        else:
            if t%n[0]:
                return float("inf")
            else:
                return t//n[0]
    
    take = minRec(ind, t-n[ind], n) + 1 if t-n[ind] >= 0 else float("inf")
    dontTake = minRec(ind-1, t, n)
    
    return min(take, dontTake)


def minMemo(ind, t, n, dp):
    if ind == 0:
        if t == 0:
            return 0
        else:
            if t%n[0]:
                return float("inf")
            else:
                return t//n[0]
    
    if dp[ind][t] != float("inf"):
        return dp[ind][t]
    
    take = minMemo(ind, t-n[ind], n, dp) + 1 if t-n[ind] >= 0 else float("inf")
    dontTake = minMemo(ind-1, t, n, dp)
    
    dp[ind][t] =  min(take, dontTake)
    return dp[ind][t]


def minDP(tar, n,):
    dp = [[ float("inf") for t in range(tar+1)]for ind in range(len(n))]

    for ind in range(len(n)):
        for t in range(tar+1):
            if ind == 0:
                if t == 0:
                    dp[ind][t] = 0
                else:
                    if t%n[0]:
                        dp[ind][t] = float("inf")
                    else:
                        dp[ind][t] = t//n[0]
            else:
                take = dp[ind][t-n[ind]] + 1 if t-n[ind] >= 0 else float("inf")
                dontTake = dp[ind-1][t]
                dp[ind][t] =  min(take, dontTake)
    return dp[len(n)-1][tar]