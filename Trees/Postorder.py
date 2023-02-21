# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        order = self.potorderRecursiveOneStack(root)
        return order
    
    def postorder(self,root, order):
        if root is None:
            return
        
        self.postorder(root.left, order)
        self.postorder(root.right, order)
        order.append(root.val)

    def potorderRecursiveTwoStacks(self, root):
        s1 = []
        s2 = []

        if root is not None:
            s1.append(root)
        
        while len(s1) != 0:
            popped = s1.pop()
            s2.append(popped.val)
            if popped.left is not None:
                s1.append(popped.left)
            if popped.right is not None:
                s1.append(popped.right)
        
        return s2[::-1]

    def potorderRecursiveOneStack(self, root):
        s = []
        final = []
        if root is not None:
            s.append(root)

        while len(s):
            while root.left is not None:
                s.append(root.left)
                root = root.left
            
            popped = root
            while(len(s) and (s[-1].right is None or s[-1].right == popped)):
                popped = s.pop()
                final.append(popped.val)
            
            if len(s) and s[-1].right is not None:
                s.append(s[-1].right)
                root = s[-1]
        return final