class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [-1] * len(nums)

        def dfs(i, highest):
            if lis[i] > -1:
                return lis[i]
            maxNum = 1
            for j in range(i, len(nums), 1):
                if nums[j] > highest:
                    maxNum = max(maxNum, 1 + dfs(j, nums[j]))
            lis[i] = maxNum
            return maxNum
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, nums[i]))
        
        return res