class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((1,0), (-1,0), (0,-1), (0,1))
        pac, atl = set(), set()

        def dfs(r, c, visited, prev):
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prev
            ):
                return
            visited.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

