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

        while gap < n and tmp.next:
            lenList += 1
            tmp = tmp.next
            gap += 1

        while tmp:
            lenList += 1
            tmp = tmp.next
            prev = curr
            curr = curr.next
        
        if lenList == n:
            head = curr #This was the main place stuck; If lenList == n, it means that the first node is the one to be removed. Hence, by assigning curr to head, you will skip that node.
            return head
        else:
            prev.next = curr.next

        return head
  
            
        
        