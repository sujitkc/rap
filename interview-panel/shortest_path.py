
INF = 1000*1000*1000
def shortest_path(n,s,AdjacencyList,Capacities,Costs,f):

    dist = [INF]*n
    dist[s] = 0

    inq = [False]*n
    queue = []
    queue.append(s)

    path = [-1]*n

    while(len(queue) > 0):
        u = queue.pop(0)
        inq[u] = False
        
        for v in AdjacencyList[u]:
            if(Capacities[u][v] > 0 and dist[v] > dist[u] + Costs[u][v]):

                dist[v] = dist[u] + Costs[u][v]
                path[v] = u

                if(inq[v] == False):
                    inq[v] = True
                    queue.append(v)
    


    return dist,path



