# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]

        while stack_p or stack_q:
            if len(stack_p) != len(stack_q):
                return False
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if not node_p and not node_q:
                continue
            
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            stack_p.append(node_p.left)
            stack_p.append(node_p.right)
            stack_q.append(node_q.left)
            stack_q.append(node_q.right)
        return True
        