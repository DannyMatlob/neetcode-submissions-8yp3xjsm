class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    self.markNeighbors(grid, row, col)
                    res += 1
        return res


    def markNeighbors(self, grid: List[List[str]], row, col) -> None:
        if grid[row][col] == "0":
            return
        
        grid[row][col] = "0"
        rows, cols = len(grid), len(grid[0])
        if row + 1 < rows:
            self.markNeighbors(grid, row + 1, col)
        if row - 1 >= 0:
            self.markNeighbors(grid, row - 1, col) 
        if col + 1 < cols:
            self.markNeighbors(grid, row, col + 1) 
        if col - 1 >= 0:
            self.markNeighbors(grid, row, col - 1) 