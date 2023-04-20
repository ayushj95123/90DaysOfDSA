#problem https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
	#return ninjaRec(points, 0, -1)
	
	# dp = [[-1 for j in range(3)] for i in range(n+1)]
	# return ninjaMemo(points, 0, -1, dp)

	return ninjaDP(points)


def ninjaRec(p, day, prev):
	if day == len(p):
		return 0
	
	first = p[day][0] + ninjaRec(p, day+1, 0) if prev !=0 else 0
	second = p[day][1] + ninjaRec(p, day+1, 1) if prev !=1 else 0
	third = p[day][2] + ninjaRec(p, day+1, 2) if prev !=2 else 0

	return max([first,second,third])

def ninjaMemo(p, day, prev, dp):
	if day == len(p):
		return 0
	
	if dp[day][prev] != -1:
		return dp[day][prev]
	
	first = p[day][0] + ninjaMemo(p, day+1, 0, dp) if prev !=0 else 0
	second = p[day][1] + ninjaMemo(p, day+1, 1, dp) if prev !=1 else 0
	third = p[day][2] + ninjaMemo(p, day+1, 2, dp) if prev !=2 else 0

	dp[day][prev] = max([first,second,third]) 
	return dp[day][prev]

def ninjaDP(p):
		
	dp = [[-1 for j in range(3)] for i in range(len(p)+1)]

	for day in range(len(p), -1, -1):
		for prev in range(3):
			
			if day == len(p):
				dp[day][prev] = 0
			
			else:
				first = p[day][0] + dp[day+1][0] if prev !=0 else 0
				second = p[day][1] + dp[day+1][1] if prev !=1 else 0
				third = p[day][2] + dp[day+1][2] if prev !=2 else 0
			
				dp[day][prev] = max([first,second,third])

	return max(dp[0])
