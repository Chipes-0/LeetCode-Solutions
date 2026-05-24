# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def LCA(root, p, q):
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)

            if left and right:
                return root

            return left if left else right
        
        def BFS(root):
            nonlocal deep
            nonlocal max_depth

            queue = [(root, 0)]
            while queue:
                node, depth = queue.pop(0)
                deep[depth].append(node)
                if node.left:
                    queue.append((node.left, depth + 1))
                    max_depth = depth + 1
                if node.right:
                    queue.append((node.right, depth + 1))
                    max_depth = depth + 1
                
    
        max_depth = 0
        deep = defaultdict(list)
        BFS(root)

        out = None
        
        if len(deep[max_depth]) == 1:
            return deep[max_depth][0]     

        lca = LCA(root, deep[max_depth].pop(), deep[max_depth].pop())
        while deep[max_depth]:
            lca = LCA(root, lca, deep[max_depth].pop())
        return lca