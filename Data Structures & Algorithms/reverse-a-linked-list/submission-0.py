# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        previous = head
        curr = head.next
        forward = None

        previous.next = None

        while curr is not None:
            forward = curr.next
            curr.next = previous
            previous = curr
            curr = forward
                
        
        head = previous

        return head
