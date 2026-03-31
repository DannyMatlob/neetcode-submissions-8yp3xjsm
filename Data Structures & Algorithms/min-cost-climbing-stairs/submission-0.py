class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 2)
        for i in range(len(cost)-1, -1, -1):
            curCost = min(cost[i] + memo[i+1], cost[i] + memo[i + 2])
            memo[i] = curCost
        print(memo)
        return min(memo[0], memo[1])