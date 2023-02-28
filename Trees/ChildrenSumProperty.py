def getChildrenSumProperty(root):
    if root is None:
        return
    
    left = root.left.val if root.left is not None else 0
    right = root.right.val if root.right is not None else 0
    
    if root.val < left + right:
        root.val = left+right
    else:
        if root.left is not None:
            root.left.val = root.val
        if root.right is not None:
            root.right.val = root.val


    getChildrenSumProperty(root.left)
    getChildrenSumProperty(root.right)

    left = root.left.val if root.left is not None else 0
    right = root.right.val if root.right is not None else 0
    
    if root.right or root.left:
        root.val = left + right
    

