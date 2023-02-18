#problem https://leetcode.com/problems/palindrome-partitioning/description/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        final = []
        self.getPartitions(s, curr, final)
        return final
    
    def getPartitions(self, s, curr, final):
        if s == "":
            final.append(curr[:])
            return

        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                curr.append(s[:i+1])
                self.getPartitions(s[i+1:], curr, final)
                curr.pop()
    
    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start<end:
            if s[start] != s[end]:
                return False
            start = start+1
            end = end -1
        return True