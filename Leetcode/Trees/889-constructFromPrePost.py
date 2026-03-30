# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_idx = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        posPost = {num:i for i,num in enumerate(postorder)}

        def helper(l,r):
            if l > r :
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx+=1

            root = TreeNode(root_val)
            if l == r:
                return root
        
            mid_value = preorder[self.pre_idx]
            mid = posPost[mid_value]

            root.left = helper(l,mid)
            root.right = helper(mid+1,r-1)

            return root
        return helper(0,len(postorder)-1)

            
            
        


