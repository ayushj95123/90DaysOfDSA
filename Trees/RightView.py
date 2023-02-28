#problem https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds = self.right(root)
        return ds

    def right(self, root):
        q = deque()
        final = []
        if root is not None:
            q.append(root)
        while len(q):
            rightElement = 0
            l = len(q)
            for i in range(l):
                popped = q.popleft()
                rightElement = popped.val
                if popped.left is not None:
                    q.append(popped.left)
                if popped.right is not None:
                    q.append(popped.right)
            final.append(rightElement)
        return final