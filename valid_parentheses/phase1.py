# in-validとなるとき
# ある種類のopen branketの出現回数が0なのにclosed branketが出てくる
# closed branketが出てきた時, open branketに他の種類のものが紛れ込んでいる
# 全ての作業が終わった後, open branketの数が0になっていない

# ↑...という回答を真っ先に思い浮かんだが, 何か考えすぎているきがした。
# 明らかにおかしいのでもう少し問題の性質をちゃんと考えてみることに
# dequeを使って最後に見たopen branketを管理するFIFOにすればいいことに気付き, 採用

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        last_seen_open_brankets = deque([])
        last_seen_open_branket = ""
        open_brankets = set(["(", "[", "{"])
        close_branket_to_open_branket = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in open_brankets:
                last_seen_open_brankets.appendleft(last_seen_open_branket)
                last_seen_open_branket = char
            
            elif char in close_branket_to_open_branket:
                if last_seen_open_branket != close_branket_to_open_branket[char]:
                    return False
                if len(last_seen_open_brankets) != 0:
                    last_seen_open_branket = last_seen_open_brankets.popleft()

        if len(last_seen_open_brankets) != 0:
            return False
        
        return True