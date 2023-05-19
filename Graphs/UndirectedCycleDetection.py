from Graph import Graph

graph = Graph(7)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 5)
graph.addEdge(3, 4)
graph.addEdge(3, 6)
graph.addEdge(5, 7)
graph.addEdge(6, 7)




class Info:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent

def isCyclic(g):
    adj = g.getAdj()
    for node in adj.keys():
        if dfs(g, node):
            return True
    
    return False
    

    


def dfs(g: Graph, start: int):
    visited = [False]* (g.v+1)
    s = []
    s.append(Info(start,None))
    visited[start] = True
    adj = g.getAdj()

    while len(s):
        popped = s.pop()
        for adjNode in adj[popped.val]:
            if visited[adjNode]:
                if popped.parent != adjNode:
                    return True
            
            else:
                s.append(Info(adjNode, popped.val))
                visited[adjNode] = True
    return False


    
print(isCyclic(graph))
