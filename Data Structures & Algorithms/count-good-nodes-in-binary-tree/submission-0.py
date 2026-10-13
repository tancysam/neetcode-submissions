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

        maxVal = 0

        def dfs(root, maxVal): 
            
            if not root:
                return 0

            maxVal = max(maxVal,root.val)
            print(maxVal)
            
            l = dfs(root.left,maxVal)
            r = dfs(root.right,maxVal)

            if root.val < maxVal:
                return l+r
            else:
                return l+r+1
        
        return dfs(root,maxVal)

            