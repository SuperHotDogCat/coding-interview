"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/50/files itertoolsでの解答と再帰によるbacktrackを見ました。再帰でのbacktrackを練習してみます。
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/57/files 

今回は全ての数が等しい前提のもとでコードを書いたが, next_permutationを用いた方が重複がある場合にも対応できるのではないかと思った。
Phase1で書いたものの時間計算量はO(Σ_{0->n}k!)という悲惨なものに, これは書いてはいけない。
要素数10で比較してみた結果
itertoolsを使った場合: 0.5979518890380859
phase1解法: 2.563912868499756 
再帰でbacktrackをする方法: 0.0003998279571533203 
とにかく似たような書いたように見えていても本当にまずいことをしていることがわかった。再帰を書くときはnaiveなフィボナッチ実装のように再帰が積み上がってないかを確認
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))

# phase1で書いたもの, 時間計算量が非常に高い, この回答はまずい気がする
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        adding_number = nums.pop()
        added_permutations = self.permute(nums) # all the permutations of nums without adding_number
        permutations: List[List[int]] = [] # all the permutations of nums
        for added_permutation in added_permutations:
            for i in range(len(added_permutation)+1):
                permutations.append(added_permutation[:i] + [adding_number] + added_permutation[i:]) 
                # insert adding_number as i-th number of added_permutations
        
        return permutations

# 再帰でbacktrack
# イメージ的には, ある要素を加える, その要素を加える前の状態に戻るを繰り返す感じだろうか

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def make_permutations(current):
            if len(current) == len(nums):
                permutations.append(current[:])
                return
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                make_permutations(current)
                current.pop()

        permutations = []
        make_permutations([])
        return permutations
