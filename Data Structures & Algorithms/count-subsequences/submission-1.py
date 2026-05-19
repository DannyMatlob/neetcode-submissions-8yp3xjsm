class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        memo = {} # key: (i, j) -> num
        # I is the pointer for where we are at in S
        # J is the pointer for where we are at in T
        # When J > len(t), we have found a complete subsequence
        def dfs(i, j):
            # Return cached value if exists
            if (i,j) in memo:
                return memo[(i,j)]
            
            # If we reach the end of T, we found a valid sequence
            if j == len(t):
                return 1
            # If we reach the end of S, we are out of letters to form a subsequence
            if i == len(s):
                return 0
            
            subres = 0
            # If the current pointers match, we can choose this letter in S
            if s[i] == t[j]:
                subres += dfs(i + 1, j + 1)

            # We can also always decide to not take this letter in S
            subres += dfs(i + 1, j)
            memo[(i,j)] = subres
            return subres
        
        return dfs(0, 0)