# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        

        while current is not None:

            if current.left is None:
                current = current.right
            else:
                pre = self.getPre(current)
                pre.right = current.right
                current.right = current.left
                current.left = None
                current = current.right
        return root
    


    def getPre(self, root):
        current = root.left
        while current.right is not None:
            current = current.right
        
        return current