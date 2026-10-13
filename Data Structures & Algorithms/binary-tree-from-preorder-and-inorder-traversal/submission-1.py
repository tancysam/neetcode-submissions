# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# root, left, right ; left, root, right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder)==0 or len(inorder)==0:
            return None
        
        currRoot = preorder[0]
        rootInorder = inorder.index(currRoot)
        inOrderLeft = inorder[0:rootInorder]
        inOrderRight = inorder[rootInorder+1:]
        preOrderLeft = preorder[1:len(inOrderLeft)+1]
        preOrderRight = preorder[len(inOrderLeft)+1:]

        l = self.buildTree(preOrderLeft,inOrderLeft)
        r = self.buildTree(preOrderRight,inOrderRight)

        root = TreeNode()
        root.val = preorder[0]

        if l is not None:
            root.left = l
        if r is not None:
            root.right = r

        return root






        
        