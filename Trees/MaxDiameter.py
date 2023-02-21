# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC: O(N)
class TreeInfo:
    def __init__(self, height = 0, maxDiameter = 0):
        self.height = height
        self.maxDiameter = maxDiameter
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        treeInfo = self.getDiameter(root)
        return treeInfo.maxDiameter

    def getDiameter(self, root):
        if root is None:
            return TreeInfo()
        
        else:
            leftInfo = self.getDiameter(root.left)
            rightInfo = self.getDiameter(root.right)

            currentHeight = max(leftInfo.height, rightInfo.height)+1

            diameter = leftInfo.height + rightInfo.height
            maxDiameter = max([diameter, leftInfo.maxDiameter, rightInfo.maxDiameter])

            return TreeInfo(currentHeight, maxDiameter)