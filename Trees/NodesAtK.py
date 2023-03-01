#problem https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        visited = {}
        self.getParents(root, None, parents)
        result  = []
        self.bfs(target, k, visited, parents, result)
        return result

    def getParents(self, root, parent, parents):
        if root:
            parents[root.val] = parent
            self.getParents(root.left, root, parents)
            self.getParents(root.right, root, parents)
    
    def bfs(self, root, target, visited, parents, result):
        q = deque()
        if root is not None:
            q.append(root)
            visited[root.val] = True
        count = 0
        while len(q) and count <= target:
            print(count)
            for  i in range(len(q)):
                popped = q.popleft()
                print(popped.val)
                if count == target:
                    result.append(popped.val)
                
                if popped.left is not None and popped.left.val not in visited:
                    q.append(popped.left)
                    visited[popped.left.val] = True
                if popped.right is not None and popped.right.val not in visited:
                    q.append(popped.right)
                    visited[popped.right.val] = True
                if  parents[popped.val] is not None and parents[popped.val].val not in visited:
                    q.append(parents[popped.val])
                    visited[parents[popped.val].val] = True
            count = count+1