class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] will store: "How many ways can we decode s starting from index i?"
        dp = {len(s): 1} 

        def dfs(i):
            # 1. Check if we already solved this sub-problem
            if i in dp:
                return dp[i]
            
            # 2. Handle the "Zero" case (invalid start)
            if s[i] == "0":
                return 0
            
            # 3. Decision 1: Decode a single digit
            res = dfs(i + 1)
            
            # 4. Decision 2: Decode two digits (10-26)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] < "7")):
                res += dfs(i + 2)
            
            # 5. Save the result in our dictionary and return it
            dp[i] = res
            return res
            
        return dfs(0)