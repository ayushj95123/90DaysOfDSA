# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #return self.insert(root, val)
        return self.insertRecursive(root, val)


    def insert(self, root, val):
        node = TreeNode(val)
        current = root
        if current is None:
            return node
        
        while True:
            if val > current.val:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            else:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
        return root

    
    def insertRecursive(self, root, val):
        if root is None:
            return TreeNode(val)
        else:
            if val > root.val:
                root.right = self.insert(root.right, val)
            else:
                root.left = self.insert(root.left, val)
            return root