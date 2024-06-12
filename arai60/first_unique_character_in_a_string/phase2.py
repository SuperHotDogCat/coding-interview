"""
reference
Exzrgsさん: https://github.com/Exzrgs/LeetCode/pull/9/files 命名を参考にした
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/28/files 
2回ループをどうにか1回ループで回せないか考えてみたが, 1回ループでまわしたあと, 辞書が順序を保存することを使わないとうまく書けないことと, 少し複雑な条件分岐が入ることを学んだ

一応, 辞書を使っている人が多いのでdictを使うようにした。入力の文字列の名前がsなのでcharもcにした
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_appear_count = defaultdict(int)
        for c in s:
            char_to_appear_count[c] += 1

        for index, c in enumerate(s):
            if char_to_appear_count[c] == 1:
                return index
        return -1

# ループを一回に済ませる
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_first_appear_index = defaultdict(int)
        duplicated = set()
        for index, c in enumerate(s):
            if c in duplicated:
                continue
            if c in char_to_first_appear_index:
                del char_to_first_appear_index[c]
                duplicated.add(c)
                continue
            char_to_first_appear_index[c] = index
        if not char_to_first_appear_index:
            return -1
        return next(iter(char_to_first_appear_index.values()))