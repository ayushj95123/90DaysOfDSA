class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp = []
        # maxi = [[]]
        newArr = sorted(nums)
        # self.getSubset(0, dp, maxi, newArr)
        # print(maxi[0])
        # return maxi[0]
        return self.getSubsetDP(newArr)

    

    def getSubset(self, ind, dp, maxi, nums):
        if ind == len(nums):
            if len(dp) > len(maxi[0]):
                maxi[0] = dp[:]
            return
        
        if len(dp) == 0 or nums[ind] % dp[-1] == 0:
            dp.append(nums[ind])
            self.getSubset(ind+1, dp, maxi, nums)
            dp.pop()
        
        self.getSubset(ind+1, dp, maxi, nums)

    

    def getSubsetDP(self, nums):
        dp = [1]*len(nums)
        hsh = [-1] * len(nums) 
        maxi = float("-inf")
        maxiInd = -1


        for i in range(1, len(nums)):
            for prev in range(i):
                if nums[i] % nums[prev] == 0:
                    if dp[prev]+1 > dp[i]:
                        dp[i] = dp[prev]+1
                        hsh[i] = prev
            if dp[i] > maxi:
                maxi = dp[i]
                maxiInd = i
        
        print("DP:", dp)
        print("HSH", hsh)
        final = []
        for i in range(dp[maxiInd]):
            final.append(nums[maxiInd])
            maxiInd = hsh[maxiInd]
        
        return (final[::-1])
        



            

        


