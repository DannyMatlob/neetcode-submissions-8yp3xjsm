class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(permutation: List[int], remaining: List[int]):
            if len(remaining) == 0:
                res.append(list(permutation))
                return
            
            for i in range(len(remaining)):
                permutation.append(remaining[i])
                dfs(permutation, remaining[0:i] + remaining[i+1:])
                permutation.pop()
        dfs([], nums)
        return res

