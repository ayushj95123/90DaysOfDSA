class Solution:

	def isMatch(self, s: str, p: str) -> bool:
		return self.wildDP(p, s)
			
	def wildDP(self, p, t):
		print("Hellp")
		dp = [[-1 for ti in range(len(t)+1)]for pi in range(len(p)+1)]

		for pi in range(len(p)+1):
			for ti in range(len(t)+1):

				if ti == 0 and pi == 0:
					dp[pi][ti] = True
	
				elif pi == 0:
					dp[pi][ti] = False
	
				elif ti == 0:
					dp[pi][ti] = True
					ind = pi-1
					for i in range(ind+1):
						if p[i] != "*":
							dp[pi][ti] = False
							break
						


				else:
					if t[ti-1] == p[pi-1]:
						dp[pi][ti] = dp[pi-1][ti-1]
					else:
						if p[pi-1] == "?":
							dp[pi][ti] = dp[pi-1][ti-1]
						elif p[pi-1] == "*":
							dp[pi][ti] = dp[pi-1][ti-1] or dp[pi][ti-1] or dp[pi-1][ti]
						else:
							dp[pi][ti] = False

		return dp[len(p)][len(t)]


	def wildRec(self, p, t, pi, ti):
		if ti < 0 and pi < 0:
			return True
	
		if pi < 0:
			return False
	
		if ti < 0:
			if not(p[0] == "*" or p[0] == "?"):
				return False
			else:
				for ind in range(1, pi+1):
					if p[ind] != "*":
						return False
				return True
	

		if t[ti] == p[pi]:
			return self.wildRec(p,t, pi-1, ti-1)
	
		else:
			if p[pi] == "?":
				return self.wildRec(p,t, pi-1, ti-1)
			elif p[pi] == "*":
				return self.wildRec(p,t, pi-1, ti-1) or self.wildRec(p,t, pi, ti-1) or self.wildRec(p,t, pi-1, ti)
			else:
				return False