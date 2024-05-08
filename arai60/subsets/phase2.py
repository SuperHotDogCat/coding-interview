"""
Reference
hayashi-ayさん: https://discord.com/channels/1084280443945353267/1200089668901937312/1222078986759311410
                https://github.com/hayashi-ay/leetcode/pull/63
shining-aiさん: https://github.com/shining-ai/leetcode/pull/51/files
ryoさん: https://github.com/ryoooooory/LeetCode/pull/5

変更点:
良い関数名が浮かばなくてrecursive_find_all_subsetsという名前にしてしまったが, recursiveはいらなくてむしろfind_all_subsetsとかmake_subsetsぐらいでいい
重複がそもそもでず, if文で処理せずに無駄な計算をせずにコードが終了するような論理順序にした書き方にすべきと感じたのでshining-aiさんのを参考に変更した。
前やったpermutationsと同じような論理のはずだが...まだ練習が足りてなさそうだと思った。

他に, itertoolのものとhayashi-ayさんのbitmask版も実装してみた
"""

# itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        for i in range(len(nums)+1):
            all_subsets.extend(itertools.combinations(nums, i))
        return all_subsets

# 再帰
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def find_all_subsets(begin, current_subset):
            all_subsets.append(current_subset.copy())
            for i in range(begin, len(nums)):
                current_subset.append(nums[i])
                find_all_subsets(i+1, current_subset)
                current_subset.pop()
        find_all_subsets(0, [])
        return all_subsets

# bitmask
# bitが立っているところを要素に入れる
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make_subset(bitmask):
            subset = []
            index = 0
            while bitmask:
                if bitmask & 1:
                    subset.append(nums[index])
                bitmask >>= 1
                index += 1
            return subset
        all_subsets = []
        for bitmask in range(2 ** len(nums)):
            all_subsets.append(make_subset(bitmask))
        return all_subsets