# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        nodes = []
        start = head

        if not start.next and n == 1:
            return None

        while head:
            nodes.append(head)
            head = head.next
        
        # [1,2,3,4] len(nodes) = 4 
        length = len(nodes)

        if n == 1: # just last val
            nodes[length-2].next = None
            return start

        elif n == length: # just first val
            return start.next

        else: # anything in between
            index = length - n
            nodes[index-1].next = nodes[index+1]
            return start
                