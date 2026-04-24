class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        res = x
        for i in range(abs(n) - 1):
            res *= x
        
        if n < 0:
            return 1/res

        return res