def inorderMorris(self, root):
    current = root
    inorder = []

    while current is not None:

        if current.left is None:
            inorder.append(current.val)
            current = current.right


        elif current.left is not None:
            poPred = self.findInorderPredecessor(current)
            if poPred.right is current:
                inorder.append(current.val)
                poPred.right = None
                current = current.right
            else:
                poPred.right = current
                current = current.left
    return inorder