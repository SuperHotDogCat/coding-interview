from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        seen_open_brankets = deque([])
        last_seen_open_branket = ""
        close_branket_to_open_branket = {")":"(", "}":"{", "]":"["}
        open_brankets = close_branket_to_open_branket.values() # cheeseNAさんを参考に
        for char in s:
            if char in open_brankets:
                # FIFO
                seen_open_brankets.append(char)
            
            elif char in close_branket_to_open_branket:
                if len(seen_open_brankets) == 0:
                    return False
                
                if seen_open_brankets.pop() != close_branket_to_open_branket[char]:
                    # 最後に見たopen branketと対応してないclose branketが出てきてしまった場合
                    return False

        # もし全ての作業を終えてもopen branketがdequeに残っていたら使い切っていないということ
        return not seen_open_brankets

"""Reference
nittocoさん: https://github.com/nittoco/leetcode/pull/5/files 
step3でopen branketを消していた。個人的にはあった方が頭がこんがらないけど, この辺は人の好みでしょうか。
dequeを使わずにlistの最後を取り出すでも良いのかとなった。dequeを使うと個人的にfifoとかするぞって宣言の気持ちがあるのですが, 
ここはソフトウェアエンジニアの方にぜひ聞いてみたいです。

cheeseNAさん: https://github.com/cheeseNA/leetcode/pull/10/files
かなり早いし読めるコードだし見習うところがありました。last_seen_open_branketと命名したい気持ちはあるけど

if last_seen_open_branket != close_branket_to_open_branket[char]:
    # 最後に見たopen branketと対応してないclose branketが出てきてしまった場合
    return False
                
if len(seen_open_brankets) != 0:
    # FIFO
    last_seen_open_branket = seen_open_brankets.popleft()

って感じにするよりかは,
if len(seen_open_brankets) == 0:
    return False
if seen_open_brankets.popleft() != close_branket_to_open_branket[char]:
    return False
にしたほうが確かにいいですね

あとreturn not seen_open_branketsと書いた方がpythonっぽいのでしょうか...?
"""