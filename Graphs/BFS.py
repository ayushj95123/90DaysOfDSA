from Graph import Graph
from collections import deque

graph = Graph(5)
graph.addEdge(1,2)
graph.addEdge(1,4)
graph.addEdge(2,3)
graph.addEdge(2,5)

adj = graph.getAdj()


def getBfs(adj, V):
    visited = [0] * (V+1)
    q = deque()
    q.append(1)
    visited[1] = True
    bfs = []

    while len(q):
        popped = q.popleft()
        bfs.append(popped)

        for adjNode in adj[popped]:
            if not visited[adjNode]:
                q.append(adjNode)
                visited[adjNode] = True
    
    print(bfs)

getBfs(adj,5)



        


