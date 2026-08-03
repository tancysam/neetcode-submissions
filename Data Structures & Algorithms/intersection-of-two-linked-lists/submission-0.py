# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a = headA
        b = headB

        visited = set()
        while a:
            visited.add(a)
            a = a.next

        print("ok",visited)

        while b:
            if b in visited:
                return b
            else:
                b = b.next
        
        return None

        


        
        