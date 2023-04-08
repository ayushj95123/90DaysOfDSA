def floorInBST(root, X):

    # Write your Code here.
	curr = root
	ceil = -1
	while curr is not None:
		if curr.data == X:
			return X
		if curr.data < X:
			ceil = curr.data
			curr = curr.right
		else:
			curr = curr.left
	return ceil