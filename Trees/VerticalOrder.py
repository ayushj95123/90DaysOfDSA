#problem https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

from queue import PriorityQueue
class Element:
    def __init__(self, node, vertical, level):
        self.node = node
        self.vertical = vertical
        self.level = level


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = self.getVertical(root)
        return final

    
    def getVertical(self, root):
        q = deque()
        d = {}
        q.append(Element(root, 0, 0))
        final = []

        while len(q):
            popped = q.popleft()

            if popped.vertical in d:
                d[popped.vertical].put((popped.level, popped.node.val))
            else:
                d[popped.vertical] = PriorityQueue()
                d[popped.vertical].put((popped.level, popped.node.val))
        
            if popped.node.left is not None:
                q.append(Element(popped.node.left, popped.vertical-1, popped.level+1))
            if popped.node.right is not None:
                q.append(Element(popped.node.right, popped.vertical+1, popped.level+1))
        
        for key in sorted(d):
            verticalEle = d[key]
            l = []
            while not verticalEle.empty():
                l.append(verticalEle.get()[1])
            
            final.append(l)
        return final