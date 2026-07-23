# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Takes cares of base case of both nodes being None
        if not p and not q:
            return True

        # If there is a difference in depth, this will return False
        elif not p or not q:
            return False

        #Recrusion for left and right cases. Left and right will be a boolean.    
        #Inspects current p and q values, and inspects the left and right obtained from recursion (one level down), then returns T/F
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)


        



            