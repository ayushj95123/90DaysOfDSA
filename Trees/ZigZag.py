#problem https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s1 = []
        s2 = []
        final = []

        if root is not None:
            s1.append(root)
        
        while len(s1) or len(s2):
            l = []
            while len(s1):
                popped = s1.pop()
                l.append(popped.val)
                if popped.left is not None:
                    s2.append(popped.left)
                if popped.right is not None:
                    s2.append(popped.right)
            if len(l):
                final.append(l)
                l = []
            while len(s2):
                popped = s2.pop()
                l.append(popped.val)
                if popped.right is not None:
                    s1.append(popped.right)
                if popped.left is not None:
                    s1.append(popped.left)
            if len(l):
                final.append(l)
                l = []
        return final