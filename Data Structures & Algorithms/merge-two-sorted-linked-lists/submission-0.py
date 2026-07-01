# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode()

        p1 = list1
        p2 = list2

        curr = sortedList

        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
            else:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            
        
        if p1 is not None:
            curr.next = p1
        elif p2 is not None:
            curr.next = p2
        else:
            pass

        return sortedList.next