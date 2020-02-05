class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0

        while queue:
            I, J, d = queue.popleft()
            print(I, J)
            for i, j in [I - 1, J], [I + 1, J], [I, J - 1], [I, J + 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    queue.append((i, j, d + 1))
                    grid[i][j] = 0
        # print(grid)
        if any(1 in row for row in grid):
            return -1
        else:
            return d
