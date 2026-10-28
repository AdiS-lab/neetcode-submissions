# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # carry variable init to 0 
        # if > 10 carry = 1

        # if not list then set = to 0

        start = ListNode(0)
        move = start
        carry = 0

        while l1 or l2 or carry:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            asum = l1_val + l2_val + carry
            
            if asum >= 10:
                move.next = ListNode(asum-10)
                carry = 1
            else: 
                move.next = ListNode(asum)
                carry = 0
            if l1:
                l1 = l1.next 

            if l2: 
                l2 = l2.next 
            move = move.next
        
        return start.next

            


                
         