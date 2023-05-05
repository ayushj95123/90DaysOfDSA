class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sortedArr = sorted(words, key = len)
        return self.chainDP(sortedArr)

    def chainDP(self, words):
        dp = [1]*len(words)
        maxi = 1
        for i in range(1, len(words)):
            for prev in range(i):
                
                if self.oneEdit(words[i], words[prev]):
                    if dp[prev]+1 > dp[i]:
                        dp[i] = dp[prev]+1
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi
    


    def oneEdit(self, s, t):
        if  len(s) != len(t) + 1:
            return False
        first = 0
        second = 0

        while first < len(s):
            if second == len(t):
                return first == len(s)-1 
            if s[first] == t[second]:
                first = first +1
                second = second +1
            else:
                first = first +1
        
        if first == len(s) and second == len(t):
            return True

        return False