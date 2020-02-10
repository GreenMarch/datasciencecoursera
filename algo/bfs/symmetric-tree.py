class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append((root, root))
# queue = collections.deque([(root, root)])
        while queue:
            t1, t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False

            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True
