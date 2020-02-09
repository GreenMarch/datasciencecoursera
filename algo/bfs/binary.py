# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            ans.append([node.val for node in queue])
            queue = [node for root in queue for node in (root.left, root.right) if node]
        return ans[::-1]

    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        current_level, next_level = [root], []
        from collections import deque
        res = deque()
        res.appendleft([root.val])

        while current_level:
            while current_level:
                parent = current_level.pop(0)
                if parent.left:
                    next_level.append(parent.left)
                if parent.right:
                    next_level.append(parent.right)

            if len(next_level) == 0:
                return res      

            res.appendleft([node.val for node in next_level])
            current_level = next_level
            next_level = []

        return res
    """
"""
107. Binary Tree Level Order Traversal II
Easy

1007

186

Add to List

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


in:[3,9,20,null,null,15,7]
out:[[15,7],[9,20],[3]]
"""