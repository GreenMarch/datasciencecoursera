class Solution:
    def countComponents(self, n, edges):
        """
        :param n: int
        :param edges: List[List[int]]
        :return: int
        """
        """
        Thought process
union find, find disjoint sets, then check how many sets there are

path compression
union by rank
be aware that after a union operation, the parent of a node might not be updated immediately
to solve this problem and avoid potential bugs, we should not rely on the raw parent representation, instead, we should call find(node) to actually obtain the correct parent/set label
dfs, bfs, if a node is not already visited, try bfs/dfs starting from this node, add the count of connected components by 1
"""
        # Simple UnionFind
        # def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})

n = 5
data = [[0,1],[1,2],[3,4]]
print(Solution().countComponents(n, data))