# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        
        nodes.sort()

        tail = ListNode(0) 
        head = tail 
        for node in nodes:
            tail.next = ListNode(node)
            tail = tail.next
        
        return head.next
        