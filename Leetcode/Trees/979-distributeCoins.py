# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.moves = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            nl = dfs(node.left) #net left coins
            nr = dfs(node.right) #net right coins
            self.moves += abs(nl) + abs(nr)

            return node.val-1 + nl + nr 
        dfs(root)
        return self.moves


