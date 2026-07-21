"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
definition for listObj

{
    oldAddress:newAddress
}
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        listObj = {}

        curr = head
        
        if head == None:
            return head
            
        newHead = Node(curr.val)
        newCurr = newHead

        while curr:
            newCurr.val = curr.val

            # hashing key old node to new node
            listObj[curr] = newCurr

            # when curr.next does not exist
            if curr.next == None:
                newCurr.next = None
            else:
                newCurr.next = Node(curr.next.val)
            
            curr = curr.next
            newCurr = newCurr.next
        
        curr = head
        newCurr = newHead

        while curr:
            if curr.random:
                newCurr.random = listObj[curr.random]
            
            curr = curr.next
            newCurr = newCurr.next
        
        return newHead

            
        
        




        
