class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 1, -1, -1):
            for j in range(nums[i], 0, -1):
                nextIdx = i + j
                if nextIdx >= len(nums): continue
                if dp[nextIdx]: 
                    dp[i] = True
                    break;
        
        return dp[0]