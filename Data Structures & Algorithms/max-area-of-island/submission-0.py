class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(i: int, j: int):
            if (i < 0 or 
                i >= len(grid) or 
                j < 0 or 
                j >= len(grid[0]) or
                grid[i][j] == 0):
                return 0

            area = 0
            if grid[i][j] == 1:
                area +=1
                grid[i][j] = 0
            
            area += dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

            if grid[i][j] == 1:
                area +=1

            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(dfs(i, j), maxArea)
        
        return maxArea