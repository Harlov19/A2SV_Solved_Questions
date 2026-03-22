# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node,parent,gparent):
            if not node:
                return 0
            _sum = 0
            if gparent and gparent.val%2 == 0:
                _sum+=node.val
            _sum+= dfs(node.left,node,parent)
            _sum+= dfs(node.right,node,parent)
            return _sum
        return dfs(root,None,None)
