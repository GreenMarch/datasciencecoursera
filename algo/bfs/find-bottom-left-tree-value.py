from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])  # queue.push()
        while queue:
            root = queue.popleft()  # queue.pop()
            if root.right:  # insert right child first
                queue.append(root.right)
            if root.left:  # insert left child
                queue.append(root.left)
        return root.val  # last value visited is our answer

"""
513. Find Bottom Left Tree Value
Medium

705

119

Add to List

Share
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""