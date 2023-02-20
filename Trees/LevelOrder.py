# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        self.getLevelOrder(root, final)
        return final
    
    def getLevelOrder(self, root, final):
        q = deque()
        if root is not None:
            q.append(root)
        
        while len(q):
            dp = []
            length = len(q)
            for i in range(length):
                pop = q.popleft()
                dp.append(pop.val)
                if pop.left is not None:
                    q.append(pop.left)
                if pop.right is not None:
                    q.append(pop.right)
            final.append(dp)