class Solution:
    def myPow(self, x: float, n: int) -> float:
        absolute_n = abs(n)
        sign_n = 1 if n >= 0 else -1
        def _positive_pow(x, n):
            # n > 0
            if n == 1:
                return x
            if n == 0:
                return 1
            
            if n % 2 == 0:
                pow_x_n_2 = _positive_pow(x, n / 2)
                return pow_x_n_2 * pow_x_n_2
            elif n % 2 == 1:
                pow_x_n_2 = _positive_pow(x, (n - 1) / 2)
                return x * pow_x_n_2 * pow_x_n_2
        
        positive_pow_x = _positive_pow(x, absolute_n)
        if sign_n > 0:
            return positive_pow_x
        else:
            return 1 / positive_pow_x