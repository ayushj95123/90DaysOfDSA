# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s= []
        self.addLeftElements(root)
 
    def next(self) -> int:
        popped = self.s.pop()
        if popped.right is not None:
            self.addLeftElements(popped.right)
        return popped.val


    def hasNext(self) -> bool:
        return len(self.s) > 0

    
    def addLeftElements(self, root):
        while root is not None:
            self.s.append(root)
            root = root.left