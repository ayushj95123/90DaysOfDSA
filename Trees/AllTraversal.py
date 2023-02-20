# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Element:
    def __init__(self,node, val):
        self.node = node
        self.val = val

class Solution:
    def allTraversals(self, root):
        s = []
        preorder = []
        inorder = []
        postorder = []
        if root is not None:
            s.append(Element(root,1))

        while len(s):
            top = s[-1]
            if top.val == 1:
                preorder.append(top.node.val)
                top.val = top.val +1
                if top.node.left is not None:
                    s.append(Element(top.node.left, 1))
            elif top.val == 2:
                inorder.append(top.node.val)
                top.val = top.val +1
                if top.node.right is not None:
                    s.append(Element(top.node.right, 1))
            elif top.val == 3:
                postorder.append(top.node.val)
                s.pop()
        print("Pre", preorder)
        print("In", inorder)
        print("Post", postorder)