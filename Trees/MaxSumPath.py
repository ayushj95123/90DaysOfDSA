#problem https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right\

class TreeInfo:
    def __init__(self, currentSum = 0, maxSum = float("-inf")):
        self.currentSum = currentSum
        self.maxSum = maxSum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        info = self.getMaxPath(root)
        return info.maxSum

    
    def getMaxPath(self, root):
        if root is None:
            return TreeInfo()
        
        else:
            leftTreeInfo = self.getMaxPath(root.left)
            rightTreeInfo = self.getMaxPath(root.right)

            currentPathSum =   leftTreeInfo.currentSum + rightTreeInfo.currentSum + root.val
            nextMaxSum = max([leftTreeInfo.maxSum, rightTreeInfo.maxSum, currentPathSum])

            currentSum = max(0,max(leftTreeInfo.currentSum, rightTreeInfo.currentSum) + root.val)

            return TreeInfo(currentSum, nextMaxSum)