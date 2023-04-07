# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.findNode(root, val)


    def findNode(self, root, val):
        if root is None:
            return root

        if root.val == val:
            return root

        if val < root.val:
            return self.findNode(root.left, val)
        return self.findNode(root.right, val)