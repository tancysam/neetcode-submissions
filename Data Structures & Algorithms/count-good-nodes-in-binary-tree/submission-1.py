# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        maxVal = float('-inf')

        def dfs(root, maxVal): 
            
            if not root:
                return 0

            currGood = 0
            if root.val>=maxVal:
                currGood = 1

            maxVal = max(maxVal,root.val)
            
            l = dfs(root.left,maxVal)
            r = dfs(root.right,maxVal)

            return l+r+currGood
        
        return dfs(root,maxVal)

            