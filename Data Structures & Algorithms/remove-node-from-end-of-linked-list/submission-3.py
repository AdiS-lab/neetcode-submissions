# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # before head 
        curr = dummy 
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        index = nodes[len(nodes)-n-1] # previous value
        index.next = index.next.next
        return dummy.next
            
        