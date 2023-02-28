#Problem : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = self.getLCA(root, p,q)
        return lca

    
    def getLCA(self, root, a, b):
        if root is None:
            return None
        if root is a or root is b:
            return root
        
        left = self.getLCA(root.left, a,b)
        right = self.getLCA(root.right, a, b)

        if left and right:
            return root
        if left :
            return left
        return right