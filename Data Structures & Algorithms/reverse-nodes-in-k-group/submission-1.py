# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy 

        while True:
            kth = self.getKth(prevGroup, k) 

            # we've reached the end
            if not kth: 
                break


            groupNext = kth.next

            # reverse linked list
            prev, start = kth.next, prevGroup.next
            while start != groupNext:
                temp = start.next
                start.next = prev
                prev = start
                start = temp 

            # change the head
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        
        return dummy.next

    def getKth(self, curr, k):
        # 3, 0
        while curr and k:
            curr = curr.next
            k -= 1  

        return curr