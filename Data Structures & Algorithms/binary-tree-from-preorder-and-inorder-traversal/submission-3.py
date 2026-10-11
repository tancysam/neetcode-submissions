# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# root, left, right ; left, root, right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorderDict = {}

        for index, item in enumerate(inorder):
            preorderDict[item] = index

        def bt(rootI, l, r):

            if l > r:
                return None

            currRoot = preorder[rootI]
            rootInorder = preorderDict[currRoot]
            
            left = bt(rootI + 1, l, rootInorder - 1)
            right = bt(rootI + (rootInorder - l)+1, rootInorder + 1, r)

            root = TreeNode()

            root.val = preorder[rootI]

            root.left = left
            root.right = right
            return root

        return bt(0,0,(len(preorder)-1))
