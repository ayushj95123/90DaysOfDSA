class TreeInfo:
    def __init__(self, mini = float("inf"), maxi = float("-inf"), isBST = True, count = 0, largest = 0):
        self.mini = mini
        self.maxi = maxi
        self.isBST = isBST
        self.count = count
        self.largest = largest

def largestBST(root):

	# Write your code here.
    result = getLargest(root)
    return result.largest

def getLargest(root):
    if root is None:
        return TreeInfo()
    
    left = getLargest(root.left)
    right = getLargest(root.right)

    if left.isBST and right.isBST and root.val > left.maxi and root.val < right.mini:
        isBST = True
        count = left.count + right.count +1
        largest = count
        mini = min(left.mini, root.val)
        maxi = max(right.maxi, root.val)
        return TreeInfo(mini, maxi, isBST, count, largest)
    else:
        return TreeInfo(float("inf"), float("-inf"), False, 0, max(left.largest, right.largest))