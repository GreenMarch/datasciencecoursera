class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return 0
            stack = []
            for c in root.children:
                stack.append(dfs(c))
            return max(stack)+1 if stack else 1

        return dfs(root)

