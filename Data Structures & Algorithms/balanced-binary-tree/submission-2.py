# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        state = True

        def subBal(root):
            if root is None:
                return 0
        
            l = subBal(root.left)
            r = subBal(root.right)

            if abs(l-r) > 1:
                nonlocal state 
                state = False
            
            return max(l,r)+1
        
        subBal(root)
        return state
