#DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorderList = []
        self.preorderIterative(root, preorderList)
        return preorderList

    #TC: O(N) SC: Auxillary space O(n)
    def preorderRecursion(self, root, preorderList):
        if root is None:
            return
        preorderList.append(root.val)
        self.preorderRecursion(root.left, preorderList)
        self.preorderRecursion(root.right, preorderList)

    
    #TC: O(N) SC: O(n)
    def preorderIterative(self,root, preorderList):
        s = []
        if root is not None:
            s.append(root)
        
        while len(s) != 0:
            popped = s.pop()
            preorderList.append(popped.val)
            if popped.right is not None:
                s.append(popped.right)
            if popped.left is not None:
                s.append(popped.left)
