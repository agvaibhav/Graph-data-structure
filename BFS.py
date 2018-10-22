from collections import defaultdict

class Graph:
    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)


    def BFS(self,s):
        visited=[False]*len(self.graph)

        q=[]

        q.append(s)
        visited[s]=True

        while q:
            s=q.pop()
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("breadth first traversal starting from vertex 2 of graph is:")
g.BFS(2)

print("BFS starting from vertex 0 is:")
g.BFS(0)
