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
        old_to_new = {}
        queue = collections.deque([node])

        new_node = Node(node.val, None)
        old_to_new[node] = new_node

        while queue:
            cur_node = queue.popleft()
            for nei in cur_node.neighbors:
                if nei not in old_to_new:
                    queue.append(nei)
                    newNei = Node(nei.val, None)
                    old_to_new[nei] = newNei
                old_to_new[cur_node].neighbors.append(old_to_new[nei])

        """
        for old,new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])
        """
        return old_to_new[node]

# O(n+m)
# O(N)

