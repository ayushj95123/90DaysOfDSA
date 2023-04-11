# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.delNodeRecursive(root, key)
        return root
    

    def delNodeRecursive(self, root, key):
        if root == None:
            return root
        if key == root.val:
            updatedTree = self.delNode(root)
            del(root)
            return updatedTree
        if key < root.val:
            root.left = self.delNodeRecursive(root.left, key)
            return root
        else:
            root.right = self.delNodeRecursive(root.right, key)
            return root

    
    def delNode(self, node):
        #case1 Leaf node
        if node.left is None and node.right is None:
            del(node)
            return None
        
        #case2 Full Node
        if node.left is not None and node.right is not None:
            leftMostOnRight = self.findLeftMost(node.right)
            leftMostOnRight.left = node.left
            return node.right
        
        #case3 only one child
        if node.left is None:
            return node.right
        else:
            return node.left
    

    def findLeftMost(self, node):
        leftMost = node
        while leftMost.left is not None:
            leftMost = leftMost.left
        return leftMost