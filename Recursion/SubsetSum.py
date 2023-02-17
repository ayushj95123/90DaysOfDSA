#Problme https://practice.geeksforgeeks.org/problems/subset-sums2234/1

#time complexity 2^n

class Solution:
    def subsetSums(self, arr, N):
		# code here
        final = []
        self.getSubsetSum(arr, N, 0, 0, final)
        return final

    def getSubsetSum(self, a, n, index = 0, summ = 0, final = []):
        if index >= n:
            final.append(summ)
            return
	    
	    #take the current element
        self.getSubsetSum(a, n, index+1, summ + a[index], final)
        self.getSubsetSum(a, n, index+1, summ, final)
	    
