class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            sum = 0
            while n > 0:
                sum += (n % 10)**2
                n = n//10
            return sum

        slow = n
        fast = next(n)
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
            
        return True if fast == 1 else False


                