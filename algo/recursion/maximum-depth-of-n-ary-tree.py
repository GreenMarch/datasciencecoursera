# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        depth = [self.maxDepth(c) for c in root.children]
        return max(depth) + 1

# root = Node(1)
# root.children = Node(3)
# root.children = Node(2)
# root.children = Node(4)
# root.children(3).children = Node(5)
# root.children(3).children = Node(6)
#
# Solution().maxDepth(root)