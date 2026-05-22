class Solution:
    def mySqrt(self, x: int) -> int:
        n = x

        if x == 0:
            return 0

        while n > x // n:
            n = (n + x // n) // 2
        return n