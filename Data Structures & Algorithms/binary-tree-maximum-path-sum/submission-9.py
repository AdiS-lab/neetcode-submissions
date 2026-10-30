# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def explore(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(explore(node.left), 0)    # drop negative branches
            right = max(explore(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        
        explore(root)
        return max_sum 