# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderList = []
        self.inorder(root, inorderList)
        return inorderList
    
    #TC: O(n) SC: Auxillary O(n)
    def inorder(self, root, inorderList):
        if root is None:
            return
        self.inorder(root.left, inorderList)
        inorderList.append(root.val)
        self.inorder(root.right, inorderList)

    #TC: O(n) SC: O(n)
    def inOrderIterative(self, root, inorderList):
        s = []
        if root is not None:
            s.append(root)
        
        while len(s) != 0:
            while root.left is not None:
                s.append(root.left)
                root = root.left
            popped = s.pop()
            inorderList.append(popped.val)
            if popped.right is not None:
                s.append(popped.right)
                root = popped.right