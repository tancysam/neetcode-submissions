# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        visited = set()

        while head.next:
            item = head.next
            if item in visited:
                return True
            else:
                visited.add(item)

            head = head.next

        return False