V = 4
INF = 9999
def floydWarshall(graph):
    dist = lambda i : map(lambda j : j , i),graph
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],min[i][k]+min[k][j])
    printSoution(dist)
def printSoution(dist):
    print("Following matrix shows the shortest dis")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s"%("INF")),
            else:
                print("%7d\t"%(dist[i][j]))
            if j == V-1:
                print("")

graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
floydWarshall(graph)
