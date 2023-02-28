#problem https://leetcode.com/problems/maximum-width-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = self.getWidth(root)
        print("Max Width", maxWidth)
        return maxWidth



    def getWidth(self, root):
        q = deque()
        if root is not None:
            q.append((root, 1))
        
        maxWidth = 0
        

        while len(q):
            position = []
            length = len(q)
            for i in range(length):
                popped = q.popleft()
                ind = popped[1]
                node = popped[0]
                position.append(ind)
                if node.left is not None:
                    q.append((node.left, 2*ind))
                if node.right is not None:
                    q.append((node.right, 2*ind+1))
            width = position[-1] - position[0] + 1
            print("Curretn level width :", width)
            maxWidth = max(maxWidth, width)
        
        return maxWidth
    
    def getWidthOptimized(self, root):
        q = deque()
        if root is not None:
            q.append((root, 1))
        
        maxWidth = 0
        

        while len(q):
            position = []
            length = len(q)
            for i in range(length):
                popped = q.popleft()
                ind = popped[1]
                node = popped[0]
                position.append(ind)
                if node.left is not None:
                    q.append((node.left, 1 if ind == 1 else 2*(ind-1) + 1))
                if node.right is not None:
                    q.append((node.right, 2 if ind == 1 else 2*(ind-1) + 2))
            width = position[-1] - position[0] + 1
            print("Curretn level width :", width)
            maxWidth = max(maxWidth, width)
    
        return maxWidth