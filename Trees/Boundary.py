from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverseBoundary(root):
    # Write your code here.
    l = []
    r = []
    le = []
    final = []
    final.append(root.data)
    left(root.left, l)
    right(root.right, r)
    leaf(root, le)

    final.extend(l)
    if le[0] is not root:
        final.extend(le)
    final.extend(r[::-1])
    return final


    pass

def left(root, ds):
    if root is None or (root.left is None and root.right is None):
        return
    ds.append(root.data)
    if root.left is not None:
        left(root.left, ds)
    elif root.right is not None:
        left(root.right, ds)

def right(root, ds):
    if root is None or (root.left is None and root.right is None):
        return
    ds.append(root.data)
    if root.right is not None:
        right(root.right, ds)
    elif root.left is not None:
        right(root.left, ds)

def leaf(root, ds):
    if root:
        if root.left is None and root.right is None:
            ds.append(root.data)
        leaf(root.left, ds)
        leaf(root.right,ds)    
