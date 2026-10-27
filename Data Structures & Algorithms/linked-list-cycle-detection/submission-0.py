# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # index = beginning of the cycle
        # map[]
        
        index = -1
        print(head)

        seen = set()

        while head:
            if head in seen:
                return True

            seen.add(head)
            head = head.next
        
        return False

        