#problem https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        self.getPermutations(nums, 0, final)
        return final
    
    def getPermutations(self, a, start = 0, final = []):
        if start >= len(a):
            final.append(a[:])
            return
        
        else:
            for i in range(start, len(a)):
                self.swap(a, start, i)
                self.getPermutations(a, start+1, final)
                self.swap(a, start, i)
    
    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp