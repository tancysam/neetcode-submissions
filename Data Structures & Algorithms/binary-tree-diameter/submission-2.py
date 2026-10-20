# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxL = 0

        def dfs(root):

            if not root:
                return 0
            
            currL = dfs(root.left)
            currR = dfs(root.right)
            nonlocal maxL
            maxL = max(maxL, currL+currR)

            return max(currL, currR) +1
        
        dfs(root)
        return maxL