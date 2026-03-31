class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxProduct = 1
        minProduct = 1
        
        for i in range(len(nums)):
            tmp = maxProduct
            maxProduct = max(nums[i], maxProduct * nums[i], minProduct * nums[i])
            minProduct = min(nums[i], tmp * nums[i], minProduct * nums[i])
            res = max(maxProduct, res)
            print(res, maxProduct, minProduct)
            if nums[i] == 0:
                maxProduct = minProduct = 1
        return res