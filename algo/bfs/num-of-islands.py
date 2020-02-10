from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft()

                        for x, y in [r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]:
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                                grid[x][y] = '#'
                                queue.append((x, y))
                    count += 1
        return count

"""
input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
output = 1
"""