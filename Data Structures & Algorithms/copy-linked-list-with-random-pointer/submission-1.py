"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # idea is creating a deep copy 
        # so next points to copy of next and random points to copy of random node
        # create 3, and point it to what already exists

        current = head

        nodes_seen = {None:None} # returns None in the case that a node points at None

        while current:
            nodes_seen[current] = Node(current.val)
            current = current.next

        current = head

        while current: 
            nodes_seen[current].next = nodes_seen[current.next]
            nodes_seen[current].random = nodes_seen[current.random]
            current = current.next

        return nodes_seen[head]
        # works without random