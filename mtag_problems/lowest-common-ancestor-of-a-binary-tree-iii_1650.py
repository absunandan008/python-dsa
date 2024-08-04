
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
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
