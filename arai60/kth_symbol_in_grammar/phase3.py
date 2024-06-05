# 再帰で解く方法を選択

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        
        previous_value = self.kthGrammar(n - 1, (k + 1) // 2)
        if k % 2 == 0:
            return 1 - previous_value
        else:
            return previous_value
