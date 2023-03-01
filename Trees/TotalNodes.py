# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        nodes = self.getCount(root)
        return nodes
    

    def getCount(self, root):
        if root:
            lh = self.getLeftHeight(root)
            rh = self.getRightHeight(root)

            if lh == rh:
                return (1<<lh)-1
            else:
                return 1 + self.getCount(root.left) + self.getCount(root.right)
        return 0
    

    def getLeftHeight(self,root):
        if root is None:
            return 0
        
        return 1 + self.getLeftHeight(root.left)
    
    def getRightHeight(self,root):
        if root is None:
            return 0
        
        return 1 + self.getRightHeight(root.right)