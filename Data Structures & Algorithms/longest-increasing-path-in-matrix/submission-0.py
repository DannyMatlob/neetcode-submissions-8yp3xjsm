class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp = [[0] * COLS for _ in range(ROWS)]
        def dfs(i, j):
            # print("Searching: ", i, j, matrix[i][j])
            maxPath = 0
            for di, dj in directions:
                if (i + di < ROWS and j + dj < COLS
                and i + di >= 0 and j + dj >= 0
                and matrix[i+di][j+dj] > matrix[i][j]):
                    # print("Going in direction: ", di, dj)
                    maxPath = max(maxPath, dfs(i + di, j + dj))
            dp[i][j] = maxPath + 1
            return dp[i][j]
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j))
                # print("-----Current Res is:", res)
        return res