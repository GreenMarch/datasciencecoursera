class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N, p = len(grid), len(grid[0]), 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    if m == 0   or grid[m-1][n] == 0: p += 1
                    if n == 0   or grid[m][n-1] == 0: p += 1
                    if n == N-1 or grid[m][n+1] == 0: p += 1
                    if m == M-1 or grid[m+1][n] == 0: p += 1
                    # print(m,n,p)
        return p

"""
463. Island Perimeter
Easy

1451

97

Add to List

Share
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""