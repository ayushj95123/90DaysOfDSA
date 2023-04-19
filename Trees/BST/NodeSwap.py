# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.middle = self.last = None
        self.prev = TreeNode(float("-inf"))
        self.inorder(root)

        if self.last is None:
            temp = self.first.val
            self.first.val = self.middle.val
            self.middle.val = temp
        else:
            temp = self.first.val
            self.first.val = self.last.val
            self.last.val = temp
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            if self.prev is not None and root.val < self.prev.val:
                if self.first is None:
                    self.first = self.prev
                    self.middle = root
                else:
                    self.last = root            
            self.prev = root
            self.inorder(root.right)
        return