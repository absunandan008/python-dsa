
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def getDepth(self, node: 'node') -> int:
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    def lowestCommonAncestorOptimal(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None
        depth_of_p = self.getDepth(p)
        depth_of_q = self.getDepth(q)

        while depth_of_p > depth_of_q:
            p = p.parent
            depth_of_p -= 1

        while depth_of_q > depth_of_p:
            q = q.parent
            depth_of_q -= 1

        while p!= q:
            p = p.parent
            q = q.parent
        return p


    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors_of_p = set()

        while p is not None:
            ancestors_of_p.add(p)
            p = p.parent

        while q is not None:
            if q in ancestors_of_p:
                return q
            q = q.parent

        return None
