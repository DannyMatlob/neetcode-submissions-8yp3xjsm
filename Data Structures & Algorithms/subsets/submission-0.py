class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.visitedSets = set()
        self.res = []

        self.dfs(nums)

        return self.res

    def dfs(self, nums: List[int]):
        numsTuple = tuple(nums)
        if numsTuple not in self.visitedSets:
            self.res.append(nums)
            self.visitedSets.add(numsTuple)

        for i in range(len(nums)):
            subset = nums[0:i] + nums[i+1:]
            self.dfs(subset)
