# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2

        strP1 = ""
        strP2 = ""

        while p1:
            strP1 = str(p1.val) + strP1
            p1 = p1.next
        
        while p2:
            strP2 = str(p2.val) + strP2
            p2 = p2.next
        
        
        sumBoth = str(int(strP1) + int(strP2))



        newHead = ListNode()
        curr = newHead

        for i in range((len(sumBoth)-1),-1,-1):
            
            curr.val = int(sumBoth[i])
            
            if i == 0:
                pass
            else:
                curr.next = ListNode()
            
            curr = curr.next




        return newHead
