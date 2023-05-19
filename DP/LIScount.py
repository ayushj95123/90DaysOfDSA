
def findNumberOfLIS(arr: List[int]) -> int:
    # write your code here
    dp,count = getLIS(arr, len(arr))
    maxi = max(dp)
    total = 0
    for i in range(len(arr)):
        if dp[i] == maxi:
            total = total + count[i]
    return total
    


def getLIS(a, n):

    count = [1]*n
    dp = [1]*n
    for i in range(n):
        for prev in range(i):
            if a[prev] < a[i]:
                if dp[prev] + 1 > dp[i]:
                    dp[i] = dp[prev] + 1
                    count[i] = count[prev]
                    
                elif dp[prev] + 1 == dp[i]:
                    count[i] = count[i] + count[prev]
                    
    
    return (dp, count)