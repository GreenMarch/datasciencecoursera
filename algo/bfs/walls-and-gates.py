from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            point = q.popleft()
            # print("point",point)
            r, c = point[0], point[1]
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if x < 0 or x >= m or y < 0 or y >= n or rooms[x][y] != 2147483647:
                    continue
                rooms[x][y] = rooms[r][c] + 1
                q.append((x, y))
        return rooms

"""
286. Walls and Gates
Medium

904

14

Add to List

Share
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""