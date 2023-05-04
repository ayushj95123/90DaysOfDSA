def lcs(s, t):
	#dp = [[-1 for j in range(len(t)+1)] for i in range(len(s)+1)]
	#return lcsMemo(s,t, len(s)-1, len(t)-1, dp)
	return lcsDP(s,t, len(s)-1, len(t)-1)



def lcsRec(s, t, si, ti):
	if si < 0 and ti < 0:
		return 0
	
	if si < 0 or ti < 0:
		return 0

	if s[si] == t[ti]:
		return 1 + lcsRec(s,t, si-1, ti-1)
	
	else:
		return max(lcsRec(s,t,si, ti-1), lcsRec(s,t,si-1, ti))


def lcsMemo(s, t, si, ti, dp):
	if si < 0 and ti < 0:
		return 0
	
	if si < 0 or ti < 0:
		return 0
	
	if dp[si][ti] != -1:
		return dp[si][ti]

	if s[si] == t[ti]:
		dp[si][ti] = 1 + lcsMemo(s,t, si-1, ti-1, dp)
	
	else:
		dp[si][ti] = max(lcsMemo(s,t,si, ti-1, dp), lcsMemo(s,t,si-1, ti, dp))
	
	return dp[si][ti]

def lcsDP(s, t, si, ti):
	dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

	for si in range(1, len(s)+1):
		for ti in range(1, len(t)+1):
			
			if s[si-1] == t[ti-1]:
				dp[si][ti] = 1 + dp[si-1][ti-1]
	
			else:
				dp[si][ti] = max(dp[si][ti-1], dp[si-1][ti])
	
	return dp[len(s)][len(t)]