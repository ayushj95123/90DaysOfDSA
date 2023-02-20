# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




## Naive solution would be to calculate the hegiht of left tree and right tree and check the difference. The time complexity would be O(N^2) for naive solution




class TreeNode:
    def __init__(self, height = 0, isBalanced = True):
        self.height = height
        self.isBalanced = isBalanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        treeNode = self.checkBalanced(root)
        return treeNode.isBalanced


    #optimized to complexity O(n)
    def checkBalanced(self, root):
        if root is None:
            return TreeNode()
        else:
            leftNode = self.checkBalanced(root.left)
            rightNode = self.checkBalanced(root.right)
            newHeight = max(leftNode.height, rightNode.height)+1
            isBalanced = leftNode.isBalanced and rightNode.isBalanced and abs(leftNode.height-rightNode.height) <=1
            return TreeNode(newHeight,isBalanced)