from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], [(root)]
        while stack:
            res.append(max(node.val for node in stack))
            stack = [child for node in stack for child in (node.left, node.right) if child]
        return res

    # def largestValues(self, root: TreeNode) -> List[int]:
    #     res, stack = [], [(root, 0)]
    #     while stack:
    #         node, depth = stack.pop()
    #         if node:
    #             if depth == len(res):
    #                 res.append(node.val)
    #             else:
    #                 res[depth] = max(res[depth], node.val)
    #             if node.left:
    #                 stack.append((node.left, depth + 1))
    #             if node.right:
    #                 stack.append((node.right, depth + 1))
    #     return res

"""
515. Find Largest Value in Each Tree Row
Medium

657

55

Add to List

Share
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
Accepted
81,885
Submissions
137,691
"""