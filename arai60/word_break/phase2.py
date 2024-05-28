"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/39/files 
自分も書いていてs[index+1-len(word):index+1]は時間計算量的にどうなのか気になった。ローリングハッシュで書き換えることを検討する。今回の問題はtop-downの方が書きやすかった...?
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/61/files
Exzrgさん: https://github.com/Exzrgs/LeetCode/pull/10/files startwithという方法もpythonにあることを学んだ。

結局最速はwordDict, sのローリングハッシュを計算してstoreしておくことになりそう。
"""

# @cacheで覚えておいて再帰 参考: shining-aiさん
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def is_segmented(start):
            if start == len(s):
                return True
            for word in wordDict:
                if s[start:start+len(word)] != word:
                    continue
                elif is_segmented(start+len(word)):
                    return True
            return False
        return is_segmented(0)

# @cacheを使わずにメモ化
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = [False for _ in range(len(s))]
        is_tokenized = [False for _ in range(len(s))]
        def check_tokenizable(start, seen, is_tokenized):
            if start == len(s):
                return 
            if seen[start]:
                return 
            seen[start] = True
            for word in wordDict:
                if s.startswith(word, start):
                    is_tokenized[start+len(word)-1] = True
                    check_tokenizable(start+len(word), seen, is_tokenized)
            return
        check_tokenizable(0, seen, is_tokenized)
        return is_tokenized[-1]
