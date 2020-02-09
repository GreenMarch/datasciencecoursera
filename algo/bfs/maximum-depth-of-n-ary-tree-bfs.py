class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = collections.deque()
        if root:
            queue.append((root, 1))
        depth = 0
        while queue:
            root, curr_depth = queue.popleft()
            if root:
                depth = max(depth, curr_depth)
                for c in root.children:
                    queue.append((c, curr_depth + 1))
        return depth
"""
class Solution(object):
    def maxDepth(self, root):
        queue = []
        if root: queue.append((root, 1))
        depth = 0
        for (node, level) in queue:
            depth = level
            queue += [(child, level+1) for child in node.children]
        return depth
"""