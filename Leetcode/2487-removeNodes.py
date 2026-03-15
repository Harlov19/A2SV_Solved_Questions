# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [head]
        curr = head.next
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            if stack:
                stack[-1].next = curr
                stack.append(curr)
            else:
                head = curr
                stack.append(curr)
            curr = curr.next
        stack[-1].next = None
        return head
        
