# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        posIn = {num: i for i, num in enumerate(inorder)}
        self.pre_idx = 0

        def helper(l_in, r_in):
            if l_in > r_in:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx+=1
            
            root = TreeNode(root_val)
            in_idx = posIn[root_val]
            
            root.left = helper(l_in,in_idx-1)
            root.right = helper(in_idx+1 ,r_in)
            
            return root

        return helper(0, len(inorder) - 1)

