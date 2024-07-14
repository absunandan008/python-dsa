
from collections import deque

def bfs_recursive(graph, queue, visited, output):
    if not queue:
        return output

    node = queue.popleft()
    output.append(node)
    ##print(node, end=' ')  # Process the node (in this case, just printing it)

    for neighbor in graph[node]:
        if neighbor and neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(graph, queue, visited, output)

# We need helper function with recursive bfs
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    output = []
    bfs_recursive(graph, queue, visited,output)
    print("BFS traversal:", output)
    #print()

# Define a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
