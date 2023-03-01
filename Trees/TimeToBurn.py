class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



def timeToBurnTree(root, start):
	mp = {}
	tar = [None]
	getParents(root, mp, start, tar)
	return bfs(tar[0], mp)

def getParents(root, mp, start, tar, parent = None):
	if root:
		if root.data == start:
			tar[0] = root
		mp[root] = parent
		getParents(root.left, mp, start, tar, root)
		getParents(root.right, mp, start, tar, root)
	return

def bfs(root, mp):
	visited = defaultdict(lambda: False, {})
	visited[root] = True
	q = deque()
	q.append(root)
	time = 0
	while(len(q)):
		
		for i in range(len(q)):
			pop = q.popleft()
			if pop.left is not None and not visited[pop.left]:
				visited[pop.left] = True
				q.append(pop.left)
			if pop.right is not None and not visited[pop.right]:
				visited[pop.right] = True
				q.append(pop.right)
			if mp[pop] and not visited[mp[pop]]:
				visited[mp[pop]] = True
				q.append(mp[pop])

				
		time += 1
	return time-1