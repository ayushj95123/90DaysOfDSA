# Problem :https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = []
        final = []
        candidates.sort()
        self.findCombinations(candidates, target, 0, dp, final)
        return final
        

    def findCombinations(self, a, target, start, dp, final):
        if target == 0:
            final.append(dp[:])
            return
        if start >= len(a) or target<0:
            return
        
        else:
            for i in range(start, len(a)):
                
                if i > start and a[i] == a[i-1]:
                    continue
                else:
                    dp.append(a[i])
                    self.findCombinations(a, target-a[i], i+1, dp, final)
                    dp.pop()