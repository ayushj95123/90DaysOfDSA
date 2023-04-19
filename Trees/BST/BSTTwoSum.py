# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        bstIterator = BSTIterator(root)
        ascNext = bstIterator.getNextAsc()
        descNext = bstIterator.getNextDesc()
        while ascNext and descNext and ascNext.val < descNext.val:
            total = ascNext.val + descNext.val
            if total == k:
                return True
            
            if total < k:
                ascNext = bstIterator.getNextAsc()
            else:
                descNext = bstIterator.getNextDesc()
            
        return False
        

class BSTIterator:
    def __init__(self, root):
        self.ascIterator = []
        self.descIterator = []
        self.addLeft(root)
        self.addRight(root)
    

    def addLeft(self, root):
        while root is not None:
            self.ascIterator.append(root)
            root = root.left

    def addRight(self, root):
        while root is not None:
            self.descIterator.append(root)
            root = root.right
    
    def getNextAsc(self):
        popped = self.ascIterator.pop()
        if popped.right is not None:
            self.addLeft(popped.right)
        return popped

    def getNextDesc(self):
        popped = self.descIterator.pop()
        if popped.left is not None:
            self.addRight(popped.left)
        return popped