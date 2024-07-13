

def dfs_recursive(graph,start,visited):
    if visited is None:
        visited = []
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph,node,visited)
    return visited
# defined a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': ['E', 'F'],
    'E': [],
    'F': []
}

output = dfs_recursive(graph,'A',[])
print("dfs_Recursive", output)