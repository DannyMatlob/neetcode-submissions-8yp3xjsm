class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curNums, curSum):
            if curSum == target:
                res.append(list(curNums))
                return
            if i == len(nums) or curSum > target:
                return

            curNums.append(nums[i])
            dfs(i, curNums, curSum + nums[i])
            curNums.pop()
            dfs(i + 1, curNums, curSum)
        
        dfs(0, [], 0)
        return res