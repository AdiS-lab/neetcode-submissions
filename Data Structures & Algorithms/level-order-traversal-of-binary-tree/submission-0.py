# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        final_arr = []

        def buildArr(root, layer):

            nonlocal final_arr

            if not root:
                return
            
            if len(final_arr) == layer: # unexplored layer
                final_arr.append([])
            
            final_arr[layer].append(root.val) # layer 0 appends [1]

            layer += 1 

            left = buildArr(root.left, layer)
            right = buildArr(root.right, layer)

            return

        temp = buildArr(root, 0)
        return final_arr

