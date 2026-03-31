class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i, sum1, sum2):
            if i == len(nums):
                if sum1 == sum2: return True
                return False
            
            return (dfs(i + 1, sum1 + nums[i], sum2) 
                    or 
                    dfs(i + 1, sum1, sum2 + nums[i])
            )
        
        return dfs(0, 0, 0)