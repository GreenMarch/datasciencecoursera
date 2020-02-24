from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()
        size_max = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    # size, size_max = 1, 1
                    print("find", i, j)
                    grid[i][j] = 0
                    size_max = max(self.bfs(i, j, grid), size_max)
                    print(i, j, size_max)
        return size_max

    def bfs(self, i, j, grid):
        q = deque([(i, j)])
        area = 1
        while q:
            i, j = q.popleft()
            for I, J in [i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]:
                if 0 <= I < len(grid) and 0 <= J < len(grid[0]) and grid[I][J] == 1:
                    grid[I][J] = 0
                    q.append((I, J))
                    area += 1
        return area
"""
695. Max Area of Island
Medium

1508

67

Add to List

Share
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""