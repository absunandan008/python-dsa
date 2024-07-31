class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1/x

        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result

    def myPow2(self, x: float, n: int) -> float:
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x*x, n//2)
            return res*x if n % 2 == 1 else res
        res = helper(x,abs(n))
        return 1/res if n < 0 else res
