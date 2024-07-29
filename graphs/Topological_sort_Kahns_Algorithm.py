import collections


def kahn_topological_sort(graph):
    #count in-degress - basically how many

    #First create a map with nodes
    # and its in-degree = 0, means it has not incoming edges
    in_degree = {i: 0 for i in graph}
    print("current in degree: ",in_degree)
    print("----------------")

    # since we have create a map with all indrees 0
    # now add the actual in degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    print("current in degree: ", in_degree)
    print("----------------")
    #now collect the  0 in-degrees in a queue
    squeue = collections.deque([u for u in graph if in_degree[u] == 0])

    Topo_Order = []  # List to store the topological order

    while squeue:
        nodgree = squeue.popleft() # Remove a node from S
        #add poped node to topological order
        Topo_Order.append(nodgree)
        print("current in topo: ", Topo_Order)
        print("----------------")
        #now get out the connected nodes from nodgree
        for connected in graph[nodgree]:
            #since we removed it from obe of the connection,
            # we can reduce the degree
            in_degree[connected] -= 1
            #keep checking if something got a zero degree again
            # if yess then add in queue because its indegree has become 0
            if in_degree[connected] == 0:
                squeue.append(connected)

    if len(Topo_Order) != len(graph):
        return "Error: Graph has at least one cycle"
    else:
        return Topo_Order


def topological_sort(graph):
    # Step 1: Compute in-degrees of all nodes
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of each node to 0
    print("current in degree: ", in_degree)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    print("current in degree: ", in_degree)
    # Step 2: Collect all nodes with in-degree 0
    S = collections.deque([u for u in graph if in_degree[u] == 0])

    L = []  # List to store the topological order

    while S:
        n = S.popleft()  # Remove a node from S
        L.append(n)  # Add n to the topological order
        print("current in topo: ", L)
        for m in graph[n]:
            in_degree[m] -= 1  # Remove edge from n to m
            if in_degree[m] == 0:
                S.append(m)  # If m has no other incoming edges, add it to S

    # Check if the graph has edges (cycle detection)
    if len(L) != len(graph):
        return "Error: Graph has at least one cycle"
    else:
        return L



# Example graph as an adjacency list
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
print("----------------")
print(kahn_topological_sort(graph))
print("----------------")

