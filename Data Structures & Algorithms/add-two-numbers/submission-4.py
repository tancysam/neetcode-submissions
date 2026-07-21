# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        carry = 0

        head = ListNode()
        prev = None
        curr = head

        while p1 or p2:

            tmp1 = p1.val if p1 else 0
            tmp2 = p2.val if p2 else 0

            tmpSum = tmp1 + tmp2 + carry

            carry = tmpSum // 10

            curr.val = tmpSum % 10

            if p1 or p2 or carry:
                curr.next = ListNode(val=None)
            
            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next

            prev = curr
            curr = curr.next
        
        if carry > 0:
            curr.val = carry
        
        if curr.val == None:
            prev.next = None
        
        
        return head

        

            
            