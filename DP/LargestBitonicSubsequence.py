def longestBitonicSequence(arr, n):
    # Write your code here.
    front = getLIS(arr,n)
    back = getLIS(arr[::-1], n)


    longest = 0
    for i in range(n):
        longest = max(longest, front[i] + back[n-i-1])
    

    return longest -1





def getLIS(a, n):

    dp = [1]*n
    for i in range(n):
        for prev in range(i):

            if a[prev] < a[i]:
                if dp[prev] + 1 > dp[i]:
                    dp[i] = dp[prev] + 1
    
    return dp