def lcs(str1, str2):
    return lcsDP(str1, str2, len(str1)-1, len(str2)-1)

def lcsDP(s, t, si, ti):
    dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    maxi = 0
    for si in range(1, len(s)+1):
        for ti in range(1, len(t)+1):
            if s[si-1] == t[ti-1]:
                dp[si][ti] = 1 + dp[si-1][ti-1]
                maxi = max(maxi, dp[si][ti])
            else:
                dp[si][ti] = 0

	
    return maxi