class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(permutation: List[int], remaining: List[int]):
            if len(remaining) == 1:
                permutation.append(remaining[0])
                res.append(list(permutation))
                permutation.pop()
                return
            
            for i in range(len(remaining)):
                permutation.append(remaining[i])
                dfs(permutation, remaining[0:i] + remaining[i+1:])
                permutation.pop()
        dfs([], nums)
        return res

