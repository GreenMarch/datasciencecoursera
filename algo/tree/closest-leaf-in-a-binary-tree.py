from collections import deque
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        # We use a depth-first search to record in our graph each edge travelled from parent to node.
        def dfs(node, par=None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        # After, we use a breadth-first search on nodes that started with a value of k, so that we are visiting nodes in order of their distance to k. When the node is a leaf (it has one outgoing edge, where the root has a "ghost" edge to null), it must be the answer.
        queue = collections.deque(node for node in graph
                                  if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

                        # stack = deque([root])
        # while stack:
        #     node = stack.pop()
        #     print("node",node)
        #     if node:
        #         if node.val == k:
        #             if node.left:
        #                 return node.left.val
        #             elif node.right:
        #                 return node.right.val
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.val)
        # return k



