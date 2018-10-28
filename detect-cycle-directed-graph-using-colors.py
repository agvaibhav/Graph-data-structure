from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def isCyclic(self):
        color=["white"]*self.v

        for i in range(self.v):
            if color[i]=="white":
                if self.DFSutil(i,color):
                    return True
        return False

    def DFSutil(self,u,color):
        color[u]="gray"
        for v in self.graph[u]:
            if color[v]=="gray":
                return True
            elif color[v]=="white" and self.DFSutil(v,color)==True:
                return True

        color[u]="black"
        return False


g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic():
    print("graph contains cycle")
else:
    print("graph does not contain cycle")
