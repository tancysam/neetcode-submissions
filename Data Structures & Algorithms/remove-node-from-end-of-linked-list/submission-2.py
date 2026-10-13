# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        tmp = head
        curr = head
        prev = head

        gap = 0
        lenList = 0

        while gap < (n-1) and tmp.next:
            lenList += 1
            tmp = tmp.next
            gap += 1

        while tmp.next:
            lenList += 1
            tmp = tmp.next
            prev = curr
            curr = curr.next
        
        print(lenList)

        if n == 0:
            head.next = None
        elif curr == tmp:
            head = None
        else:
            prev.next = tmp

        return head
  
            
        
        