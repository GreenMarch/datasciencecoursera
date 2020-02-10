# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 111. Minimum Depth of Binary Tree
# bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append((root, 1))
        d_min = 1
        while queue:
            node_depth = queue.pop(0)
            node_curr = node_depth[0]
            d_curr = node_depth[1]
            if not node_curr.left and not node_curr.right:
                return d_curr
            if node_curr.left:
                queue.append((node_curr.left, d_curr + 1))
            if node_curr.right:
                queue.append((node_curr.right, d_curr + 1))

        return d_min


from collections import deque


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node_deque = deque([(root, 1), ])
        # stack.append((root, 1))
        min_depth = 1
        while node_deque:
            node_curr, depth_curr = node_deque.popleft()
            children = [node_curr.left, node_curr.right]
            if not any(children):
                return depth_curr
            for c in children:
                if c:
                    node_deque.append((c, depth_curr + 1))
        return min_depth


"""
111. Minimum Depth of Binary Tree
Easy

1009

583

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""