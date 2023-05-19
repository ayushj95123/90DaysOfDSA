class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = {}
    
    def addEdge(self, u, v):
        if u in self.adj:
            self.adj[u].append(v)
        else:
            self.adj[u] = [v]
        
        if v in self.adj:
            self.adj[v].append(u)
        else:
            self.adj[v] = [u]
    

    def addEdges(self, edges):
        start  = edges[0]
        end = edges[1]

        for i in range(len(start)):
            u = start[i]
            v = end[i]
            self.addEdge(u,v)
    

    def printGraph(self):
        print(self.adj)
        for (u, ends) in self.adj.items():
            for v in ends:
                print(u, "---", v)
    
    def getAdj(self):
        return self.adj






