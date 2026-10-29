# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # first thoughts are DFS
        # recurse down and return total lengths of each pass, should be compared at each node that splits and then max will persist

        return self.compareNodes(root, 0)

    def compareNodes(self, root: Optional[TreeNode], path_length):
        max_length = 0

        if not root:
            return path_length

        path_length += 1

        right_length = self.compareNodes(root.right, path_length)
        left_length  = self.compareNodes(root.left, path_length)
        
        max_length = max(right_length, left_length, max_length)

        return max_length