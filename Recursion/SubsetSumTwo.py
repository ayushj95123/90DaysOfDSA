#problem https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        dp = []
        nums.sort()
        self.getPowerSet(nums, 0, dp, final)
        return final
    

    def getPowerSet(self, a, index, dp, final):

        final.append(dp[:])

        if index >= len(a):
            return
    
        for i in range(index, len(a)):
            if i > index and a[i] == a[i-1]:
                continue
            
            dp.append(a[i])
            self.getPowerSet(a, i+1, dp, final)
            dp.pop()