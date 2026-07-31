# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #recursively search through root.left and root.right
        #once it is found that any node happens to hit equal to either p or q values, return True
        # upon first meeting either 1. both l and r to be true or either l or r and curr to be true, lca = that root
        # elif l or r is true, return True
        # else, return the curr state
        # return lca

        lca = root.right
        def searcher(root,p,q):

            if root is None:
                return False
            
            l = searcher(root.left, p, q)
            r = searcher(root.right, p, q)
            curr = root.val == p.val or root.val == q.val
        
            if (l and r) or ((l or r) and curr):
                nonlocal lca
                lca = root
                return -1
            elif l or r:
                return True
            return curr

        searcher(root,p,q)
        return lca
