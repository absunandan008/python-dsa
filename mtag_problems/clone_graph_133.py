"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    """
    Solution is 2 step
    first create a dictionary
    then dfs through graph
    add old node as key and new node as value in dict
    then loop key and values in dict , basically old and new
    for each neighbor of old, attach neighbor of new from taking from dictionary
    return dict[firstoldnode]
    """
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        oldtoNew = {}
        stack = [node]

        while stack:
            current_node = stack.pop()
            newNode = Node(current_node.val)
            oldtoNew[current_node] = newNode

            for nei in current_node.neighbors:
                if nei not in oldtoNew:
                    stack.append(nei)

        for old,new in oldtoNew.items():
            for nei in old.neighbors:
                new.neighbors.append(oldtoNew[nei])
        return oldtoNew[node]

