class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            incl1 = incl2 = False
            # Include the next letter of s1
            if i < len(s1) and s1[i] == s3[k]:
                incl1 = dfs(i + 1, j, k + 1)
            # Include the next letter of s2
            if j < len(s2) and s2[j] == s3[k]:
                incl2 = dfs(i, j + 1, k + 1)

            dp[(i, j, k)] = incl1 or incl2
            return dp[(i, j, k)]
        
        return dfs(0, 0, 0)