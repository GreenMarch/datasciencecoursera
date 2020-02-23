class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        p_land = set()
        a_land = set()
        R, C = len(matrix), len(matrix[0])

        def spread(i, j, land):
            land.add((i, j))
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if (0 <= x < R and 0 <= y < C and matrix[x][y] >= matrix[i][j]
                        and (x, y) not in land):
                    spread(x, y, land)

        for i in range(R):
            spread(i, 0, p_land)
            spread(i, C - 1, a_land)
        for j in range(C):
            spread(0, j, p_land)
            spread(R - 1, j, a_land)
        return list(p_land & a_land)


"""
class Solution:
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0:
            return []

        m, n = len(matrix), len(matrix[0])

        def height(tile):
            (i, j) = tile
            return matrix[i][j]

        def neighbours(tile):
            (i, j) = tile
            return [
                (i + a, j + b)
                for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= i + a < m
                if 0 <= j + b < n
            ]

        def find_basin(drains):
            queue = drains
            basin = set()
            while queue:
                tile = queue.pop()
                basin.add(tile)
                queue.update(
                    nb
                    for nb in neighbours(tile)
                    if nb not in basin
                    if height(nb) >= height(tile)
                )
            return basin

        top_edge    = set((  0,   j) for j in range(n))
        right_edge  = set((  i, n-1) for i in range(m))
        bottom_edge = set((m-1,   j) for j in range(n))
        left_edge   = set((  i,   0) for i in range(m))

        atlantic_basin = find_basin(bottom_edge | right_edge)
        pacific_basin  = find_basin(top_edge | left_edge)

        watershed = pacific_basin & atlantic_basin

        return list(watershed)


"""

"""
417. Pacific Atlantic Water Flow
Medium

967

184

Add to List

Share
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
data = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(data))