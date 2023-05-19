from Graph import Graph
from collections import deque

graph = Graph(5)
graph.addEdge(1,2)
graph.addEdge(1,4)
graph.addEdge(2,3)
graph.addEdge(2,5)

adj = graph.getAdj()


def getDFS(adj, V):
    visited = [False] * (V+1)
    q = []
    q.append(1)
    visited[1] = True
    dfs = []

    while len(q):
        popped = q.pop()
        dfs.append(popped)
        for adjNode in sorted(adj[popped], reverse = True):
            if not visited[adjNode]:
                q.append(adjNode)
                visited[adjNode] = True
    
    print(dfs)

getDFS(adj,5)