class Solution:

    def lca(self, node, p, q):
        if node is None:
            return q
        if node.val < q.val and node.val > p.val:
            return node
        if node.val < p.val:
            return self.lca(node.right, p, q)
        if node.val > q.val:
            return self.lca(node.left, p, q)
        return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        

        return self.lca(root, p, q)