from collections import deque
class Solution:
    def numIslands(self, grid):
        """
        :param grid: List[List[str]]
        :return: int
        """
        if not grid:
            return 0
        count = 0
        # queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # queue.append((i, j))
                    self.dfs(grid, i, j)
                    # while queue:
                    # r, c = queue.popleft()
                    # for x, y in [r - 1, c],[r + 1, c],[r, c - 1],[r, c + 1]:
                    #     # print("x, y", x, y)
                    #     if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    #         grid[x][y] = "0"
                    #         queue.append((x,y))
                    count = count + 1  # increment the number of islands
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft()
                        for x, y in [r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]:
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                                queue.append((x, y))
                                grid[x][y] = "$"
                    count += 1
        return count

        """


"""
input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
output = 1
"""
