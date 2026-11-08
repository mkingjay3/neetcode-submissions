# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, size):
            if(root is None):
                return(size)
            l1 = depth(root.left, size+1)
            l2 = depth(root.right, size+1)

            return(max(l1, l2))
        return(depth(root, 0))
        

        
        
        