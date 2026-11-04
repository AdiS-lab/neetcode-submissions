"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}                      # original -> copy

        def dfs(n):
            if n in clones:
                return clones[n]         # reuse the existing copy
            copy = Node(n.val)
            clones[n] = copy             # register BEFORE recursing
            for nb in n.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy

        return dfs(node)            