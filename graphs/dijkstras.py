import heapq

infinity = float("inf")


def make_graph():
    # tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3 , 'E'), (2, 'D')],
        'C': [(1, 'B'), (4 , 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')]
    }

##Implementation with heap, if no start is given then use A
def dijkstras_heap(G, start='A'):
    #this is the Map we initialize with all the distances from Start node(vertex) to all nodes(vertexs)
    # We will initializwe all as infinity because at start all the nodes are infinity
    shortest_paths = {}

    #Once we have visited a vertex(node), we know
    # that we have found its shortest distance from start(source) node(vertex)
    # this set will keep those vertexes(nodes)
    visited = set()

    # Heap to keep the nodes which are not visited but sorted by minimum distance first
    heap = []


    for node in G.keys():
        shortest_paths[node] = infinity

    shortest_paths[start] = 0
    #visited.add(start)
    heapq.heappush(heap, (0, start))

    while heap:
        # take out lowest dist from heap
        dist, node = heapq.heappop(heap)
        #add the node of that path t0 heap because we visited it
        visited.add(node)

        #now calculate the new paths for its neighboring nodes
        for neighbor in G[node]:
            #calculate the distance from current node to neighbor node
            cost, to_node = neighbor
            # if the new neighbor is not already visited then we need to check
            # if in the Map for all the distances, the new path is lower than what is saved in current
            if to_node not in visited:
                if dist + cost < shortest_paths[to_node]:
                    # if it is lower , then we update the map
                    # and also push it on heap again to till we find the shortest
                    shortest_paths[to_node] = dist + cost
                    heapq.heappush(heap, (shortest_paths[to_node], to_node))
    return shortest_paths


def dijkstras_heap1(G, start='A'):
    shortest_paths = {}
    visited = set()
    heap = []

    for node in G.keys():
        shortest_paths[node] = infinity

    shortest_paths[start] = 0
    visited.add(start)

    heapq.heappush(heap, (0, start))

    while heap:
        (distance, node) = heapq.heappop(heap)
        visited.add(node)

        for edge in G[node]:
            cost, to_node = edge

            if (to_node not in visited) and (distance + cost < shortest_paths[to_node]):
                shortest_paths[to_node] = distance + cost
                heapq.heappush(heap, (shortest_paths[to_node], to_node))

    return shortest_paths






def main():
    G = make_graph()
    start = 'A'

    #shortest_paths = dijkstras(G, start)
    shortest_paths_using_heap = dijkstras_heap(G, start)

    #print(f'Shortest path from {start}: {shortest_paths}')
    print(f'Shortest path from {start} using heap: {shortest_paths_using_heap}')


main()