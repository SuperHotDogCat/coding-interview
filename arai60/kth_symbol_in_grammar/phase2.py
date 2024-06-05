"""
Reference:
Mike0121: https://github.com/Mike0121/LeetCode/pull/18/files
再帰で書く書き方, 僕がphase1で書いたやり方は移動順を取り出してきて根から辿る方法だが, こっちだと明示的にfor文を書かなくてもかける

Exzrgs: https://github.com/Exzrgs/LeetCode/pull/12/files
shining-ai: https://github.com/shining-ai/leetcode/pull/46/files
kを1で表した時の数の1の数と反転回数に注目, bitcountを用いて解く
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/46/files
親を表す単語が問題文にないことに注意して命名を行う
"""

# k = (k-1) // 2 + 1がk = (k+1) // 2でまとめられることに気づきまとめる
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        moves = deque([]) # 0: move left 1: move right
        # store the order from the leaf
        for i in range(n-1):
            if (k - 1) % 2 == 0:
                moves.appendleft(0)
            else:
                moves.appendleft(1)
            k = (k + 1) // 2 
        kth_symbol = 0
        for move in moves:
            # move 0 kth_symbol 0 -> 0
            # move 1 kth_symbol 0 -> 1
            # move 0 kth_symbol 1 -> 1
            # move 1 kth_symbol 1 -> 0
            kth_symbol = kth_symbol ^ move
        
        return kth_symbol

# 再帰
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        
        previous_value = self.kthGrammar(n - 1, (k + 1) // 2)
        
        if k % 2 == 0:
            return 1 - previous_value
        else:
            return previous_value

# bit count
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() % 2
