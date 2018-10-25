from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def isCyclic(self):
        visited=[False]*self.v
        recstack=[False]*self.v

        for node in range(self.v):
            if visited[node]==False:
                if self.isCyclicUtil(node,visited,recstack)==True:
                    return True
        return False

    def isCyclicUtil(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,recstack)==True:
                    return True
            elif recstack[i]==True:
                return True

        recstack[v]=False
        return False


g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic(): 
    print ("Graph has a cycle")
else: 
    print ("Graph has no cycle")
