# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # essentially spaced out by 1
        # ceil(len(list) /2) = # of top vals 
        if not head:
            return

        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        
        print(nodes)
        start, end = 0, len(nodes) - 1 

        print(start, end)

        while start < end:
            nodes[start].next = nodes[end]
            start += 1
            if start == end:
                break

            nodes[end].next = nodes[start]
            end -= 1            
        
        nodes[start].next = None
