class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(d, i, j):
            if (i < 0 or 
                i >= len(grid) or 
                j < 0 or 
                j >= len(grid[0]) or
                grid[i][j] < d):
                return
            
            grid[i][j] = d
            dfs(d + 1, i + 1, j)
            dfs(d + 1, i - 1, j)
            dfs(d + 1, i, j + 1)
            dfs(d + 1, i, j - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: dfs(0, i, j)