# in-validとなるとき
# ある種類のopen bracketの出現回数が0なのにclosed bracketが出てくる
# closed bracketが出てきた時, open bracketに他の種類のものが紛れ込んでいる
# 全ての作業が終わった後, open bracketの数が0になっていない

# ↑...という回答を真っ先に思い浮かんだが, 何か考えすぎているきがした。
# 明らかにおかしいのでもう少し問題の性質をちゃんと考えてみることに
# dequeを使って最後に見たopen bracketを管理するFIFOにすればいいことに気付き, 採用

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        last_seen_open_brackets = deque([])
        last_seen_open_bracket = ""
        open_brackets = set(["(", "[", "{"])
        close_bracket_to_open_bracket = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in open_brackets:
                last_seen_open_brackets.appendleft(last_seen_open_bracket)
                last_seen_open_bracket = char
            
            elif char in close_bracket_to_open_bracket:
                if last_seen_open_bracket != close_bracket_to_open_bracket[char]:
                    return False
                if len(last_seen_open_brackets) != 0:
                    last_seen_open_bracket = last_seen_open_brackets.popleft()

        if len(last_seen_open_brackets) != 0:
            return False
        
        return True