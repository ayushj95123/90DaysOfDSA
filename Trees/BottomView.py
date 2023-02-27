from collections import deque
def getBottomViews(root):
    if root is None:
        return []
    q = deque()
    q.append((root, 0))

    d = {}
    final = []

    while len(q):
        popped = q.popleft()
        node = popped[0]
        vertical = popped[1]

 
        d[vertical] = node.data
        
        if node.left is not None:
            q.append((node.left, vertical-1))
        if node.right is not None:
            q.append((node.right, vertical+1))
    
    for key in sorted(d):
        final.append(d[key])
    
    return final