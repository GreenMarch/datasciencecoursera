from collections import deque


class Solution:
    def numDistinctIslands(self, grid):
        """
        :param grid: 2d array
        :return: int
        """

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                island = []
                front = [(i, j)]

                while front:
                    nxt = []
                    for x, y in front:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == 1:
                            grid[x][y] = 0
                            island.append((x - i, y - j))  # minus the current (i,j) in the big for loop
                            for m, n in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                                nxt.append((m, n))
                    front = nxt
                if island and str(island) not in islands:
                    islands.add(str(island))
        return len(islands)

data = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(Solution().numDistinctIslands(data))