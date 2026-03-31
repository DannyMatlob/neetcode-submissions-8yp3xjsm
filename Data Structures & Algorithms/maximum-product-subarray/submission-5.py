class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = -math.inf
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums), 1):
                print(j)
                product *= nums[j]
                maxProduct = max(maxProduct, product)
        return maxProduct