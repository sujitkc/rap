import shortest_path as ShortestPath

INF = 1000*1000*1000
def SolveMinCostMaxFlow(N,edges,source,sink):

    K = INF
    AdjacencyList = [[] for i in range(N)]
    Costs = [[0 for i in range(N)] for j in range(N)]
    Capacities = [[0 for i in range(N)] for j in range(N)]


    # edge -> (from,to,capacity,cost) 
    for e in edges:
        AdjacencyList[e[0]].append(e[1])
        AdjacencyList[e[1]].append(e[0])
        Capacities[e[0]][e[1]] = e[2]
        Capacities[e[1]][e[0]] = 0
        Costs[e[0]][e[1]] = e[3]
        Costs[e[1]][e[0]] = -e[3]


    FlowMap = [[0 for i in range(N)] for j in range(N)]
    flow = 0
    cost = 0

    while(flow < K):

        dist,path = ShortestPath.shortest_path(N,source,AdjacencyList,Capacities,Costs,FlowMap)

        if(dist[sink] == INF):
            break

        f = K- flow
        curr = sink
        while(curr != source):
            f = min(f,Capacities[path[curr]][curr])
            curr = path[curr]

        flow += f
        cost += dist[sink]

        curr = sink
        while(curr != source):
            Capacities[path[curr]][curr] -= f
            Capacities[curr][path[curr]] += f
            FlowMap[path[curr]][curr] += f

            curr = path[curr]


    return FlowMap,cost
            

# if __name__ == "__main__":

#     # Define the directed graph for the flow.
#     start_nodes = [0,0] + [1,1,2,2] + [3,4]
#     end_nodes =   [1,2] + [3,4,3,4] + [5,5]
#     capacities =  [1,1] + [1,1,1,1] + [1,1]
#     costs      =  [0,0] + [4,2,6,3] + [0,0]

#     source = 0
#     sink = 5

#     edges = []
#     for i in range(len(start_nodes)):
#         edges.append((start_nodes[i],end_nodes[i],capacities[i],costs[i]))
    
#     Flow,cost = min_cost_max_flow(6,edges,source,sink)

#     print(cost)