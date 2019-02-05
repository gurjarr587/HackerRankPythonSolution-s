from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        print(self.graph[u].append(v))

    def BFS(self,s):
        visited = [False] * (len(self.graph))
        print(visited)
        queue = []
        queue.append(s)
        print(queue)

        visited[s] = True
        while queue:
            print(queue)
            s = queue.pop(0)
            print(s,end=" ")
            print(self.graph)
            for i in self.graph[s]:

                if visited[i] == False:
                    queue.append(i)
                    print(queue)
                    visited[i]=True


g = Graph()

g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(1, 2)
g.addEdge(3, 3)
print("following is BFS")
g.BFS(2)
