# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        counter = 0
        while counter < n and fast.next:
            fast = fast.next
            counter += 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
 
        
        if n == 0:
            return head
        elif slow == fast:
            head = None
            return head
        else:
            
            return head
            