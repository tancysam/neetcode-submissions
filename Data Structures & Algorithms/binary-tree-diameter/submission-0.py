# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxD = 0
        if root is None:
            return 0

        l = self.diameterOfBinaryTree(root.left) + 1
        r = self.diameterOfBinaryTree(root.right) + 1

        maxD = max(maxD,l,r)
        return maxD