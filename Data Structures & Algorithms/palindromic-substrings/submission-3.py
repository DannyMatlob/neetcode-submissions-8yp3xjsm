class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == True):
                    print(s[i:j+1], " is a palindrome")
                    dp[i][j] = True
                    
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True: res+=1
        return res