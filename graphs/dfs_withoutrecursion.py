
## DFS uses stack to push one node at a time and then take it out
# and find both children of that node and put it in stack. Then take out one children,
# and repeat the process till reached end for a current children
# then come back to second children
def dfs(graph, start_node):
    #where we push node to visit
    stack = [start_node]
    #where we know that node is visited
    visited = set([])
    #Output of traversal
    outputOrder = []

    while stack:
        current = stack.pop()
        outputOrder.append(current)

        for neighbor in graph[current]:
            if neighbor and neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return outputOrder

# create a graph
graph = {
    'A': ['B', 'C'],
    'B': [],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': [],
    'F': [],
}

outputOrder = dfs(graph, 'A')
print("outputOrder: ", outputOrder)