# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dq = deque()
        def visit(node):
            if node is None: return
            dq.append(node)
            visit(node.left)
            visit(node.right)
        visit(root)

        if dq: 
            head = dq.popleft()
            prev = head
        while dq:
            cur = dq.popleft()
            prev.left = None
            prev.right = cur
            prev= cur
