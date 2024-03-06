"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.getNodeDepth(p)
        q_depth = self.getNodeDepth(q)

        if p_depth > q_depth:
            for _ in range(p_depth - q_depth):
                p = p.parent
        else:
            for _ in range(q_depth - p_depth):
                q = q.parent

        while p != q:
            p = p.parent
            q = q.parent
        return p

    def getNodeDepth(self, p):
        depth = 0

        while p.parent:
            depth += 1
            p = p.parent

        return depth
