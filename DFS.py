from collections import defaultdict

def DFS(g, s):
    visited = [False] * len(g.graph)
    vertices = []
    DFS_util(g, s, visited, vertices)
    return vertices

def Conn_Comp(g,s):
    visited = [False] * len(g.graph)
    id_g = [0] * len(g.graph)
    c = 0
    for v in g.graph[s]:
        if visited[v] == False:
            c += 1
            DFScom(s, c, visited, id_g)
    return id_g

def DFScom(s, c, visited, id_g):
    visited[s] = True
    id_g[s] = c
    for t in g.graph[s]:
        if visited[t] == False:
            DFScom(t, c, visited, id_g)

def DFS_util(g, s, visited, vertices):
    vertices.append(s)
    visited[s] = True
    for v in g.graph[s]:
        if visited[v] == False:
            DFS_util(g, v, visited, vertices)

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

g = Graph()
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
print(DFS(g, 4))
print(Conn_Comp(g,3))
