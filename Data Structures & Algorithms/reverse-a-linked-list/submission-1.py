# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next # next node
            curr.next = prev # point curr node to previous
            prev = curr # prev = current Node
            curr = nxt # increment forward

        return prev
            

# 0 --> 1 --> 2 -> 3
# 1. append (stack) 
# 2. sorting is long
# 3. deleting/appending is 0(1) 