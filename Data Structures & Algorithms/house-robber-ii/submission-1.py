class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.oldRob(nums[1:]), self.oldRob(nums[:-1]))
    
    def oldRob(self, nums):
        memo = [0] * (len(nums) + 2)

        for i in range(len(nums)-1, -1, -1):
            memo[i] = max(memo[i+1], nums[i] + memo[i+2])
        print(memo)
        return memo[0]
        