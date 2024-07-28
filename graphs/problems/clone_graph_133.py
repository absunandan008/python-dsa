"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from typing import Optional
class Solution:
    def cloneGraphRecursive(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        if node is None:
            return None

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # we need to assign to a new node here
        start = node
        oldToNew = {}
        stack = [start]

        while stack:
            node = stack.pop()
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                if nei not in oldToNew:
                    stack.append(nei)

        for old, new in oldToNew.items():
            for nei in old.neighbors:
                new_nei = oldToNew[nei]
                new.neighbors.append(new_nei)
        # Time Complexity: O(V+E)
        # Space Complexity: O(V)
        return oldToNew[start]
