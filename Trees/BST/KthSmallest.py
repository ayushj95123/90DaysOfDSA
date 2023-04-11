# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Status:
    def __init__(self, k, smallest):
        self.k = k
        self.smallest = smallest

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        status = Status(k, root.val)
        self.inOrder(root, status)
        return status.smallest


    def inOrder(self, root, status):
        if root is None:
            return
        self.inOrder(root.left, status)
        if status.k > 0:
            status.k = status.k-1
            status.smallest = root.val
            self.inOrder(root.right, status)