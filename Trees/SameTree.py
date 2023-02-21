#Problem : https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSame(p,q)
    
    def isSame(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        
        if a.val != b.val:
            return False
        
        if self.isSame(a.left, b.left) and self.isSame(a.right, b.right):
            return True
        
        return False