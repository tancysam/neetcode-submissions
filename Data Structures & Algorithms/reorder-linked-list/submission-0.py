# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        p1 = head
        p2 = head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        previous = None
        curr = p1.next
        forward = None
        p1.next = None
        while curr:
            forward = curr.next
            curr.next = previous
            previous = curr
            curr = forward
        

        first = head
        second = previous

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        

