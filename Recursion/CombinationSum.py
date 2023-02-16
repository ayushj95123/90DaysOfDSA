#Problem Link https://leetcode.com/problems/combination-sum/
# Time complexity 2^n
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        dp = []
        self.findCombinations(candidates, target, 0, dp, final)
        return final



    def findCombinations(self, a, target, index = 0, dp = [], final = []):
        if target < 0:
            return
        if  index >= len(a):
            if target == 0:
                final.append(dp[:])
            return

        #take the current element
        dp.append(a[index])
        self.findCombinations(a,target-a[index], index, dp, final)

        #Dont take the current element and move forward
        dp.pop()
        self.findCombinations(a, target, index+1, dp, final)