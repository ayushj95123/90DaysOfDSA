#problem https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = [0]
        return self.construct(preorder, ind, inorder)

    def construct(self, preorder, ind, inorder):
        if len(inorder) == 0:
            return None
        currentNode = TreeNode(preorder[ind[0]])

        ind[0] = ind[0] + 1

        rootIndex = self.findIndex(inorder, currentNode.val)

        currentNode.left = self.construct(preorder, ind, inorder[:rootIndex])
        currentNode.right = self.construct(preorder, ind, inorder[rootIndex+1:])

        return currentNode
        

    def findIndex(self, a, val):
        for i in range(len(a)):
            if a[i] == val:
                return i
        return -1