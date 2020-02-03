class Solution:
    # pass
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0  # to count number of islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count = count + 1  # increment the number of islands
        return count

    def dfs(self, grid, i, j):
        # skip the dfs check if the current element is water or previosuly marked land
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # mark this newly visited land element
        grid[i][j] = '@'
        # check all the adjacent elements to find land
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


"""
            # not pass
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
                    
    def isValid(self, grid, r, c):
        if r >= 0 and r <= len(grid) and c >= 0 and c <=len(grid[0]):
            return True
        else:
            False
    
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if self.isValid(grid, nr, nc) and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc)
"""
"""
200. Number of Islands
Medium

3429

126

Favorite

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
