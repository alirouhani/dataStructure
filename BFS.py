from collections import defaultdict

def BFS(g, s):
    visited = [False] * len(g.graph)
    vertices = []
    q = [s]    
    visited[s] = True
    vertices.append(s)
    while len(q) > 0: 
        u = q.pop(0)
        for v in g.graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                vertices.append(v)
    return vertices

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
g = Graph()
g.add_edge(0, 1)
g.add_edge(2, 3)
g. add_edge(4, 5)
g.add_edge(1, 2)
g.add_edge(6, 3)
g.add_edge(3, 5)
g.add_edge(0, 5)
g.add_edge(5, 0)
g.add_edge(1, 3)
g. add_edge(4, 0)
g.add_edge(5, 6)
g.add_edge(5, 4)
g.add_edge(0, 3)
g.add_edge(1, 6)
g.add_edge(2, 0)
print(BFS(g, 4))
