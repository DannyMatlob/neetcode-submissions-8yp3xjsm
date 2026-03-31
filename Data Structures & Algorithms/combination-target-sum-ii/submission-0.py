class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curList:List[int], idx:int, remaining: int):
            if remaining == 0:
                res.append(list(curList))
                return
            
            if remaining < 0 or idx >= len(candidates):
                return
            # 2, 2, 3 target 5
            curList.append(candidates[idx])
            dfs(curList, idx + 1, remaining - candidates[idx])
            curList.pop()

            nextIdx = idx
            while nextIdx+1 < len(candidates) and candidates[nextIdx] == candidates[nextIdx+1]:
                nextIdx += 1
            
            dfs(curList, nextIdx + 1, remaining)
            
        dfs([], 0, target)    

        return res