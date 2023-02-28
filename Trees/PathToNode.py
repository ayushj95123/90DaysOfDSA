#problem https://www.interviewbit.com/problems/path-to-given-node/
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        path = []
        self.getPath(A, B, path)
        return path

    
    def getPath(self, root, tar, path):
        if root is None:
            return False
        path.append(root.val)
        if root.val  == tar:
            return True
        else:
                
            if self.getPath(root.left, tar, path) or self.getPath(root.right, tar, path): 
                return True

            path.pop()
            return False