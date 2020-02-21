from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        res = []
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.left:
                    stack.append(root.left)

                if root.right:
                    stack.append(root.right)

        return res[::-1]

"""
145. Binary Tree Postorder Traversal
Hard

1362

69

Add to List

Share
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

in = [1,null,2,3]
out = [3,2,1]
"""