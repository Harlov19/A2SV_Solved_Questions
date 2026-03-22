# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs (curr_sum,node,targetSum):
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right:
                return curr_sum == targetSum

            left =  dfs(curr_sum ,node.left,targetSum)
            right = dfs(curr_sum ,node.right,targetSum)
            return left or right
          
        return dfs(0,root,targetSum)
         
