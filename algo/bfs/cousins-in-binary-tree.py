# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {}
        depth = {}
        queue = []
        if root:
            queue.append((root, 0, 1)) # node, parent, depth
        while queue:
            node_par_d = queue.pop(0)
            node_curr = node_par_d[0]
            parent_curr = node_par_d[1]
            d_curr = node_par_d[2]
            parent[node_curr.val] = parent_curr
            depth[node_curr.val] = d_curr
            if node_curr.left:
                queue.append((node_curr.left, node_curr, d_curr + 1))
            if node_curr.right:
                queue.append((node_curr.right, node_curr, d_curr + 1))
        return depth[x] == depth[y] and parent[x] != parent[y]