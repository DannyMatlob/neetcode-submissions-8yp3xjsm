class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1: return False
        half = totalSum // 2

        memo = {}
        def dfs(i, sum):
            if (i, sum) in memo:
                return memo[(i, sum)]
            if i == len(nums):
                if sum == half: return True
                return False
            
            res = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)
            memo[(i, sum)] = res
            return res
        
        return dfs(0, 0)