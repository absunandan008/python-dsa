from collections import deque

def bfs(graph, root):
    # in BFS we use queue but in DFS we use stack. Stack gives us LIFO and queue give us FIFO.
    #
    queue = deque([root])
    visited = set([root])
    outputordered = []

    while queue:
        current = queue.popleft()
        outputordered.append(current)

        for neighbor in graph[current]:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return outputordered

# defined a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': ['E', 'F'],
    'E': [],
    'F': []
}
print("BFS Graph:", bfs(graph, 'A'))
