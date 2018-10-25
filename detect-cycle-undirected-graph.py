from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def isCyclic(self):
        visited=[False]*self.v
        for i in range(self.v):
            if visited[i]==False:
                if(self.isCyclicUtil(i,visited,-1)):
                    return True

        return False

    def isCyclicUtil(self,node,visited,parent):
        visited[node]=True

        for i in self.graph[node]:
            if visited[i]==False:
                if(self.isCyclicUtil(i,visited,node)):
                    return True

            elif parent!=i:
                return True

        return False



g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")

g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
if g1.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
