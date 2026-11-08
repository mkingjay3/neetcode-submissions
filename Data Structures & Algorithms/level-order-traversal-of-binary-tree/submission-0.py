# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lis = [] 

        def next(root, index):
            if(root is None):
                return; 
            if(index == len(lis)):
                lis.append([])
            lis[index].append(root.val)
            next(root.left, index+1)
            next(root.right, index+1)

        next(root, 0)
        return(lis)



        
        