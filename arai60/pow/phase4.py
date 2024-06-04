# binary exponentiationについて実装してみる
# 参考: https://github.com/hayashi-ay/leetcode/pull/41/files

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary_pow(x, n):
            powered_x = 1
            while n > 0:
                if n & 1:
                    powered_x *= x
                x *= x
                n = n >> 1
            return powered_x
        if n < 0:
            return 1 / binary_pow(x, -n)
        return binary_pow(x, n)