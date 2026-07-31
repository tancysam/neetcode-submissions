# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        
        def heightOfTree(root):
            if root is None:
                return 0

            l = heightOfTree(root.left) 
            r = heightOfTree(root.right) 
            nonlocal maxD
            maxD = max(l+r, maxD)

            return max(l,r)+1
        
        heightOfTree(root)
        return maxD