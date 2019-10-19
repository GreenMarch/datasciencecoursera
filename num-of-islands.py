class Solution:
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
