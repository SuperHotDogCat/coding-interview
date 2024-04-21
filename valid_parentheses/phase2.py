class Solution:
    def isValid(self, s: str) -> bool:
        seen_open_brackets = []
        close_bracket_to_open_bracket = {")":"(", "}":"{", "]":"["}
        open_brackets = close_bracket_to_open_bracket.values() # cheeseNAさんを参考に
        for char in s:
            if char in open_brackets:
                # FIFO
                seen_open_brackets.append(char)
            
            elif char in close_bracket_to_open_bracket:
                if len(seen_open_brackets) == 0:
                    return False
                
                if seen_open_brackets.pop() != close_bracket_to_open_bracket[char]:
                    # 最後に見たopen bracketと対応してないclose bracketが出てきてしまった場合
                    return False

        # もし全ての作業を終えてもopen bracketがdequeに残っていたら使い切っていないということ
        return not seen_open_brackets

"""Reference
nittocoさん: https://github.com/nittoco/leetcode/pull/5/files 
step3でopen bracketを消していた。個人的にはあった方が頭がこんがらないけど, この辺は人の好みでしょうか。
dequeを使わずにlistの最後を取り出すでも良いのかとなった。

cheeseNAさん: https://github.com/cheeseNA/leetcode/pull/10/files
かなり早いし読めるコードだし見習うところがありました。last_seen_open_bracketと命名したい気持ちはあるけど

if last_seen_open_bracket != close_bracket_to_open_bracket[char]:
    # 最後に見たopen bracketと対応してないclose bracketが出てきてしまった場合
    return False
                
if len(seen_open_brackets) != 0:
    # FIFO
    last_seen_open_bracket = seen_open_brackets.popleft()

って感じにするよりかは,
if len(seen_open_brackets) == 0:
    return False
if seen_open_brackets.popleft() != close_bracket_to_open_bracket[char]:
    return False
にしたほうが確かにいいですね

あとreturn not seen_open_bracketsと書いた方がpythonっぽいのでしょうか...?
"""