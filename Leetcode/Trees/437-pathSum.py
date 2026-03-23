# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        _map = defaultdict(int)
        _map[0] = 1
        def helper(node,running_sum,_map):
            if not node:
                return 0
            
            running_sum+= node.val
            
            count = 0
            count += _map[running_sum-targetSum] 
            _map[running_sum]+=1
            count+= ( 
                 helper(node.left,running_sum,_map)+
                 helper(node.right,running_sum,_map)
                   )
            
            _map[running_sum]-=1
            return count

        return helper(root,0,_map)
        
