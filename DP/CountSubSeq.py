mod = 10**9+7

def subsequenceCounting(t: str, s: str, lt: int, ls: int) -> int:
    #return subCountRec(t,s,len(t)-1, len(s)-1)
	dp = [[-1 for ti in range(len(t))]for si in range(len(s))]
	#result = subCountMemo(t,s,len(t)-1, len(s)-1, dp)
	#print(dp)
	#return result

	return subCountDP(t,s)


def subCountRec(t,s,ti, si):
	if si < 0:
		return 1
	if ti < 0:
		return 0
	
	if t[ti] == s[si]:
		match = subCountRec(t,s,ti-1, si-1)
		unmatch = subCountRec(t,s,ti-1, si)
		return match + unmatch
	else:
		return subCountRec(t,s,ti-1, si)


def subCountMemo(t,s,ti, si, dp):
	if si < 0:
		return 1
	if ti < 0:
		return 0
	
	if dp[si][ti] != -1:
		return dp[si][ti]
		
	
	if t[ti] == s[si]:
		match = subCountMemo(t,s,ti-1, si-1, dp)
		unmatch = subCountMemo(t,s,ti-1, si, dp)
		dp[si][ti] = match + unmatch
	else:
		dp[si][ti] = subCountMemo(t,s,ti-1, si, dp)
	
	return dp[si][ti]

def subCountDP(t,s):
	dp = [[0 for ti in range(len(t)+1)]for si in range(len(s)+1)]
	dp[0] = [1]*(len(t)+1)


	for si in range(1, len(s)+1):
		for ti in range(1, len(t)+1):
			if t[ti-1] == s[si-1]:
				match = dp[si-1][ti-1]
				unmatch = dp[si][ti-1]
				dp[si][ti] = (match + unmatch)%mod
			else:
				dp[si][ti] = dp[si][ti-1]%mod

	return dp[len(s)][len(t)]