'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # Write your code here.
    ceil = x 
    current = root
    found = 0
    while current is not None:
        if current.data == x:
            ceil = x
            found = 1
            break
        if current.data > x:
            ceil = current.data
            current = current.left
        else:
            current = current.right
    
    if ceil == x:
        return x if found else -1
    return ceil