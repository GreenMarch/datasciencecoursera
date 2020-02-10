# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {}
        depth = {}

        def dfs(node, par=None):
            if node:
                depth[node.val] = depth[par.val] + 1 if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]

"""
993. Cousins in Binary Tree
Easy

400

28

Add to List

Share
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = TreeNode(4)
root.right.left = None
root.right.right = TreeNode(5)

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Solution().isCousins(root, 4, 5)
#Solution().getImportance_bfs(e, i)
"""