# 2-line Recursion. In most tree problems, try recursion first.

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))


# BFS (use a queue, the last level we see will be the depth)

class Solution(object):
    def maxDepth(self, root):
        queue = []
        if root: queue.append((root, 1))
        depth = 0
        for (node, level) in queue:
            depth = level
            queue += [(child, level+1) for child in node.children]
        return depth



# DFS (use a stack, use max to update depth)

class Solution(object):
    def maxDepth(self, root):
        stack = []
        if root: stack.append((root, 0))
        depth = 0
        while stack:
            (node, d) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d+1))
        return depth

class Solution {
    public:
        int

    maxDepth(Node * root)
    {
    if (root == nullptr)
    return 0;
    int
    depth = 0;
    for (auto child: root->children) depth = max(depth, maxDepth(child));
    return 1 + depth;

}
};