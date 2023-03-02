# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        q = deque()
        serialized = []
        if root is not None:
            q.append(root)
            serialized.append(str(root.val))
            serialized.append(" ")

        while len(q):
            for i in range(len(q)):
                popped = q.popleft()
                if popped.left is not None:
                    q.append(popped.left)
                    serialized.append(str(popped.left.val))
                    serialized.append(" ")
                else:
                    serialized.append("#")
                    serialized.append(" ")
                if popped.right is not None:
                    q.append(popped.right)
                    serialized.append(str(popped.right.val))
                    serialized.append(" ")
                else:
                    serialized.append("#")
                    serialized.append(" ")

        return "".join(serialized)
                

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None
        
        data = data.split(" ")
        q = deque()
        index = 0
        root = TreeNode(data[index])
        q.append(root)

        while len(q):
            for i in range(len(q)):
                pop = q.popleft()
                index = index+1
                
                left = data[index]
                if left == "#":
                    pop.left = None
                else:
                    pop.left = TreeNode(left)
                    q.append(pop.left)
                

                index = index+1
                right = data[index]
                if right == "#":
                    pop.right = None
                else:
                    pop.right = TreeNode(right)
                    q.append(pop.right)
                
        return root