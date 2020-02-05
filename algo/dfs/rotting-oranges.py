class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = []
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))
        d = 0
        while queue:
            i, j, d = queue.pop(0)
            for i, j in [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    grid[i][j] = 2
                    queue.append((i, j, d + 1))
        if any(1 in row for row in grid):
            return -1
        return d

