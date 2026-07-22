# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def subBal(root):
            if root is None:
                return 0
        
            l = subBal(root.left)
            r = subBal(root.right)

            if abs(l-r) > 1 or l == -1 or r == -1:
                return -1
                
            return max(l,r)+1
        
        curr = subBal(root)
        return False if curr == -1 else True
        