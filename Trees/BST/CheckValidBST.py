# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))
    

    def isValid(self, root, lower, higher):
        if root is None:
            return True
        if root.val <= lower or root.val >= higher:
            return False
        
        if not self.isValid(root.left, lower, root.val):
            return False
        
        return self.isValid(root.right, root.val, higher)
