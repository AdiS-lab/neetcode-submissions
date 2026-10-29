# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        start = root

        def invertNodes(root: Optional[TreeNode]):

            if not root.left and not root.right:
                return

            temp = root.left
            root.left = root.right
            root.right = temp
            
            if root.left: 
                invertNodes(root.left)
            
            if root.right:
                invertNodes(root.right)
        
        invertNodes(root)

        return start

        # we have to recurse down somehow

        