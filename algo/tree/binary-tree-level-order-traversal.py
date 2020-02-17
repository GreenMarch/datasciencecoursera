# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(node, level):
            # start the current level
            if len(res) == level:
                res.append([])
            # append the current node value
            res[level].append(node.val)
            # process child nodes for the next level
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return res


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = 0

        def bfs(node, level):
            queue = deque([root, ])
            while queue:
                # start the current level
                res.append([])
                # number of elements in the current level
                level_length = len(queue)

                for i in range(level_length):
                    node = queue.popleft()
                    # fulfill the current level
                    res[level].append(node.val)

                    # add child nodes of the current level
                    # in the queue for the next level
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                # go to next level
                level += 1
            return res

        bfs(root, 0)
        return bfs


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            res.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                res[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return res



"""
102. Binary Tree Level Order Traversal
Medium

2220

59

Add to List

Share
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""