# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ind = [len(postorder)-1]
        return self.construct(postorder, ind, inorder)


    def construct(self, postorder, ind, inorder):
        if len(inorder) == 0:
            return None

        currentNode = TreeNode(postorder[ind[0]])

        ind[0] = ind[0] - 1

        rootIndex = self.findIndex(inorder, currentNode.val)
        currentNode.right = self.construct(postorder, ind, inorder[rootIndex+1:])
        currentNode.left = self.construct(postorder, ind, inorder[:rootIndex])
        

        return currentNode
        

    def findIndex(self, a, val):
        for i in range(len(a)):
            if a[i] == val:
                return i
        return -1