class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        print(dp)
        dp[m-1][n-1] = 1
        print(dp)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                print(dp)
                print(" ----")
                if i < m - 1:
                    dp[i][j] += dp[i + 1][j]
                if j < n - 1:
                    dp[i][j] += dp[i][j + 1]
        print(dp)
        return dp[0][0]