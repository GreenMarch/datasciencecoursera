class Solution(object):
    import heapq
    def maxDepth(self, root):
        pqueue = []
        if root: heapq.heappush(pqueue, (root, 1))
        depth = 0
        while pqueue:
            (node, d) = heapq.heappop(pqueue)
            depth = max(depth, d)
            for child in node.children:
                pqueue.append((child, d+1))
        return depth

