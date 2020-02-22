# not dfs, in-order use stack
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

# # preorder
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
        # stack, res = deque([root]), []
        # while stack:
        #     root = stack.pop()
        #     if root:
        #         res.append(root.val)
        #         if root.right:
        #             stack.append(root.right)
        #         if root.left:
        #             stack.append(root.left)
        # return res

#     # post order
#         stack, res = deque([root]), []
#         while stack:
#             root = stack.pop()
#             if root:
#                 res.append(root.val)
#                 if root.left:
#                     stack.append(root.left)
#                 if root.right:
#                     stack.append(root.right)
#         return res[::-1]

"""
94. Binary Tree Inorder Traversal
Medium

2479

103

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""