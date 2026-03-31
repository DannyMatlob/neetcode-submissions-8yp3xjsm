class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(subset: List[int], idx: int):
            if idx == len(nums): 
                res.append(list(subset))
                return
            
            subset.append(nums[idx])
            backtrack(subset, idx + 1)
            subset.pop()
        
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx+=1
    
            backtrack(subset, idx + 1)
        backtrack([], 0)
        return res