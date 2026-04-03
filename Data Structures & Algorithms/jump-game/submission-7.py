class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 1, -1, -1):
            for j in range(nums[i]):
                jumpIdx = (nums[i] - j) + i
                if jumpIdx > len(nums) - 1: continue
                if jumpIdx == len(nums) - 1 or dp[jumpIdx]:
                    dp[i] = True
        
        return dp[0]