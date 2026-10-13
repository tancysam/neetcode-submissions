# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)

        if root.left and root.right:
            return l and r and root.left.val < root.val < root.right.val
        elif root.left and root.right is None:
            return root.left.val < root.val 
        elif root.right and root.left is None:
            return root.right.val > root.val
        else:
            return True

        #(root.left is None and root.right) or (root.right is None and root.left)
