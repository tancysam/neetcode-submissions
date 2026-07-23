# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Takes cares of base case of both nodes being None
        if p is None and q is None:
            return True

        # If there is a difference in depth, this will return False
        elif p is None and q or p and q is None:
            return False

        #Recrusion for left and right cases. Left and right will be a boolean.
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right,q.right)
        
        #Inspects current p and q values, and inspects the left and right obtained from recursion (one level down), then returns T/F
        return (p.val == q.val) and left and right


        



            