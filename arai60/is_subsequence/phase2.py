"""
Reference
go-to untrappedさん: https://github.com/goto-untrapped/Arai60/pull/19/files 正規表現の実装を一回はやってみます
shining-aiさん: https://github.com/shining-ai/leetcode/pull/57/files 
昔読んだ自然言語処理の本で現在のポインターの指すところをポインターだとかカーソルだとか命名していたのでカーソルって命名している癖が抜けてないので修正


問題は解けたが, なんだかDFAとかなんとか教育的なことを話しているぞ...?
https://news.ycombinator.com/item?id=37422355
while文で回している人が多かったが, t_indexはどのみち1増えていくので, for文で実装する方針にした。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_index = 0
        for c in t:
            if c == s[s_index]:
                s_index += 1
            if s_index >= len(s):
                return True
        return False

# 正規表現
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ""
        for c in s:
            pattern += ".*" + c
        return re.match(pattern, t) != None